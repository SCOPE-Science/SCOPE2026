#!/usr/bin/env python3
"""Verify the three-nonterminal counterexample to Algorithm 4.4.

The grammar is
    A1 -> A2 A3
    A2 -> x1
    A3 -> x1'
and the group is the free group on x1,x2,x3.  The script implements the
published K^k recurrence on U = Sigma^* x T and checks the line-7 test.
"""

def reduce_T(word):
    stack = []
    for token in word:
        if stack and token.endswith("'") and stack[-1] == token[:-1]:
            stack.pop()
        else:
            stack.append(token)
    return tuple(stack)

def mul_u(left, right):
    terminal = left[0] + right[0]
    tword = reduce_T(left[1] + right[1])
    return (terminal, tword)

def free_reduce(word):
    stack = []
    inv = {"x1": "x1'", "x1'": "x1",
           "x2": "x2'", "x2'": "x2",
           "x3": "x3'", "x3'": "x3"}
    for token in word:
        if stack and inv[token] == stack[-1]:
            stack.pop()
        else:
            stack.append(token)
    return tuple(stack)

# Vertices 0,1,2,3 are A1,A2,A3,Z.
N = 4
K = [[set() for _ in range(N)] for _ in range(N)]
K[0][1].add(((), ("A3",)))       # A1 -> A2, label <epsilon,A3>
K[3][2].add(((), ("A3'",)))      # Z  -> A3, label <epsilon,A3'>
K[1][3].add((("x1",), ()))       # A2 -> Z,  label <x1,e>
K[2][3].add((("x1'",), ()))      # A3 -> Z,  label <x1',e>

for k in range(N):
    old = K
    new = [[set(old[i][j]) for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for u in old[i][k]:
                for v in old[k][j]:
                    new[i][j].add(mul_u(u, v))
    K = new

identity_u = ((), ())
derivation_label = (("x1", "x1'"), ())
language_word = ("x1", "x1'")

print("free_group_reduction:", free_reduce(language_word))
print("language_is_contained:", free_reduce(language_word) == ())
print("derivation_label_present:", derivation_label in K[0][3])
print("g_final_1Z_cardinality:", len(K[0][3]))
print("g_final_1Z_is_identity_singleton:", K[0][3] == {identity_u})
print("algorithm_line_7_rejects:",
      K[0][3] != set() and K[0][3] != {identity_u})

assert free_reduce(language_word) == ()
assert derivation_label in K[0][3]
assert K[0][3] != {identity_u}
assert K[0][3] != set()
