# Exact arithmetic checks for the dimension proof.

incident_boundary_dim = 3 + 4
double_line_boundary_upper = 4 + 1 + 1
pair_component_dim = 11
hilb_component_dim = 8
generic_fibre_lower = pair_component_dim - hilb_component_dim
intersection_dim_lower = incident_boundary_dim + generic_fibre_lower
intersection_dim_upper = pair_component_dim - 1
reflexive_component_dim = 11
t_component_dim = 15

assert incident_boundary_dim == 7
assert double_line_boundary_upper == 6
assert double_line_boundary_upper < incident_boundary_dim

assert generic_fibre_lower == 3
assert intersection_dim_lower == 10
assert intersection_dim_upper == 10
assert intersection_dim_lower == intersection_dim_upper

intersection_dim = intersection_dim_lower
assert reflexive_component_dim - intersection_dim == 1
assert t_component_dim - intersection_dim == 5

print(f"incident_boundary_dim={incident_boundary_dim}")
print(f"double_line_boundary_dim_upper={double_line_boundary_upper}")
print(f"generic_fibre_dim_lower={generic_fibre_lower}")
print(f"pair_component_intersection_dim={intersection_dim}")
print(f"reflexive_component_codim={reflexive_component_dim-intersection_dim}")
print(f"T_component_codim={t_component_dim-intersection_dim}")
print("VERIFY_OK")
