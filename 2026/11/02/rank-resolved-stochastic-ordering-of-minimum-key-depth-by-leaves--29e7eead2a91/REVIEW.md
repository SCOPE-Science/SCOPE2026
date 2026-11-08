# Independent mathematical audit

## correctness

PASS

Uniform random continuous insertion priorities yield independent relative ranks R_k and record-low indicators A_k=1{R_k=1}, so D_n=Σ_{k≥2}A_k. A key is a leaf iff its priority is a local maximum among immediate inorder neighbors; translating to consecutive ranks gives explicit local B_i. For 3≤i<n, a uniformly distributed admissible rank triple has conditioned positive tails 3/(i+1),3/[i(i+1)],0, dominated by the independent record triple. Endpoint and i=2 conditions are checked separately. All upper-tail orders follow by independent convolution; the covariance formulas telescope to (n−2)(n+1)/(12n(n−1)). Independent enumeration over all 5,910 permutations (6+24+120+720+5040) for n=3..7 confirmed every conditional upper tail and covariance. Local-peak 2-dependence gives Var L=2n/45+O(1), hence stated correlation. The proof, rather than enumeration, handles arbitrary n.

## originality

PASS

Classical BST leaf/shape patterns and Ji (2023) Eulerian–Stirling generating functions treat aggregate permutation record/peak statistics. The inspected positions in the primary texts do not state the separate leaf-by-position conditional stochastic order with opposite sign only at key 1. Published Resultary near matches concern random recursive trees, not BSTs; those do not imply the position-conditioned claim. The summed covariance might be derivable from known aggregate polynomials and is not treated as standalone novelty.

## value

PASS

A complete key-position stochastic comparison is stronger than covariance and applies to all monotone functions of the minimum-key depth. It exposes how a single positive endpoint association outweighs all negative prescribed-other-key associations, giving a sharp structural dependence theorem for a canonical search tree model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
