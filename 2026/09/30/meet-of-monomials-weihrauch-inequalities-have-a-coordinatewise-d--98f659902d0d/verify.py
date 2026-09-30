from itertools import product, combinations

def graph_from_family(family):
    vertices = []
    components = []
    for component_index, exponent in enumerate(family):
        component = []
        for color, multiplicity in enumerate(exponent):
            for local_index in range(multiplicity):
                vertex = (component_index, color, local_index)
                vertices.append(vertex)
                component.append(vertex)
        components.append(tuple(component))
    colors = {vertex: vertex[1] for vertex in vertices}
    return tuple(vertices), tuple(components), colors

def exact_reduction(left, right, total):
    left_vertices, left_components, left_colors = graph_from_family(left)
    right_vertices, right_components, right_colors = graph_from_family(right)

    choices = []
    for vertex in right_vertices:
        same_color = [
            target for target in left_vertices
            if left_colors[target] == right_colors[vertex]
        ]
        if total:
            if not same_color:
                return False
            choices.append(same_color)
        else:
            choices.append([None] + same_color)

    for values in product(*choices):
        mapping = dict(zip(right_vertices, values))
        valid = True
        for right_component in right_components:
            image = {
                mapping[v] for v in right_component
                if mapping[v] is not None
            }
            if not any(
                set(left_component).issubset(image)
                for left_component in left_components
            ):
                valid = False
                break
        if valid:
            return True
    return False

def closed_form(left, right, total):
    dominance = all(
        any(
            all(a <= b for a, b in zip(alpha, beta))
            for alpha in left
        )
        for beta in right
    )
    if not dominance:
        return False
    if not total:
        return True

    left_support = {
        i for alpha in left
        for i, value in enumerate(alpha)
        if value > 0
    }
    right_support = {
        i for beta in right
        for i, value in enumerate(beta)
        if value > 0
    }
    return right_support <= left_support

vectors = [
    vector
    for vector in product(range(3), repeat=2)
    if 0 < sum(vector) <= 3
]
families = []
for size in (1, 2):
    families.extend(combinations(vectors, size))

checked = 0
for left in families:
    for right in families:
        if sum(map(sum, left)) + sum(map(sum, right)) > 8:
            continue
        for total in (False, True):
            exact = exact_reduction(left, right, total)
            formula = closed_form(left, right, total)
            assert exact == formula, (
                left, right, total, exact, formula
            )
            checked += 1

assert checked == 1242
print("VERIFY_OK", checked)
