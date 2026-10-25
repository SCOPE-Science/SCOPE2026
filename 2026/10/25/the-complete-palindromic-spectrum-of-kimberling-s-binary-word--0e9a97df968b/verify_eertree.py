#!/usr/bin/env python3
"""Independent palindrome-tree corroboration on a long prefix.

This bounded computation corroborates the finite-window proof; it is not
used to infer absence of arbitrarily long palindromes from sampled data.
"""
import json

phi = {'0':'01', '1':'02', '2':'0'}
f = {'0':'10','1':'0','2':'1'}
pi = {'0':'100','1':'101','2':'10'}
T = '0'
while len(T) < 100000:
    T = ''.join(phi[ch] for ch in T)
B_f = '0'+''.join(f[ch] for ch in T)
B_pi = '0'+''.join(pi[ch] for ch in T)
B = B_f[:100000]
assert B == B_pi[:100000]
# Eertree nodes: -1 length root and 0 length root.
lengths = [-1, 0]
links = [0, 0]
edges = [{}, {}]
last = 1
seq = []
created_at = []
for i,letter in enumerate(B):
    seq.append(letter)
    node = last
    while i-1-lengths[node] < 0 or seq[i-1-lengths[node]] != letter:
        node = links[node]
    if letter in edges[node]:
        last = edges[node][letter]
        continue
    new_id = len(lengths)
    lengths.append(lengths[node] + 2)
    links.append(0)
    edges.append({})
    edges[node][letter] = new_id
    created_at.append(i+1)
    if lengths[new_id] == 1:
        links[new_id] = 1
        last = new_id
        continue
    suffix = links[node]
    while i-1-lengths[suffix] < 0 or seq[i-1-lengths[suffix]] != letter:
        suffix = links[suffix]
    links[new_id] = edges[suffix][letter]
    last = new_id
assert len(lengths)-2 == 15
assert max(lengths) == 9
assert max(created_at) == 25
print(json.dumps({'prefix_length':len(B),'independent_morphism_prefix_match':True,
                  'eertree_distinct_nonempty_palindromes':len(lengths)-2,
                  'eertree_max_palindrome_length':max(lengths),
                  'last_new_palindrome_ends_at_position':max(created_at)},
                  sort_keys=True, indent=2))
