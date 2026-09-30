# Finite-stage spectra of the Obermeyer–Winter Jiang–Su diagonals are pairwise non-homeomorphic graphs

## Context

Obermeyer and Winter construct the Jiang–Su algebra as an inductive limit of entangled-matrix-cone dimension-drop algebras and obtain a C*-diagonal with one-dimensional non-locally-connected spectrum. Their Proposition 5.1 describes each finite-stage diagonal spectrum as a quotient. This record extracts elementary topological invariants of that quotient. It does not claim priority beyond that concrete calculation.

## Definitions

For L>=2 let X_L be the spectrum described in Proposition 5.1: the quotient of
\[
\{1,\dots,L\}\times\{0,\dots,L\}\times[0,1]
\]
by the stated endpoint identifications. Write R_j for the class of 1-endpoints with second coordinate j and C_i for the 0-endpoint class containing (i,0,0).

## Theorem

For every L>=2, X_L is a connected finite multigraph with
\[
V=2L+1,\qquad E=L(L+1),\qquad b_1=L(L-1).
\]
Moreover
\[
\max_{x\in X_L}\#\pi_0(X_L\setminus\{x\})=L,
\]
attained at R_0. Consequently L is recovered from the homeomorphism type of X_L, so X_L and X_{L'} are not homeomorphic when L!=L'.

## Proof

The 1-endpoints form L+1 classes R_0,...,R_L. The 0-endpoints form L classes C_1,...,C_L. There are no 0/1 identifications.

For j=0, the interval e_{i,0} joins C_i to R_0. For each j>=1, all L intervals e_{i,j} join C_j to R_j, giving an L-fold parallel bundle. Hence V=2L+1 and E=L(L+1).

The edges e_{i,0}, together with one chosen edge from every parallel bundle, form a spanning tree, so the graph is connected. Euler's formula gives
\[
b_1=E-V+1=L(L-1).
\]

For punctures:
- removing R_0 leaves the L disjoint blocks consisting of C_j, R_j, and their parallel edges, so there are L components;
- removing C_i isolates R_i from the rest, giving two components;
- removing R_j with j>=1 leaves C_j attached to R_0, so the graph remains connected;
- an interior point of e_{i,0} is a bridge cut and gives two components;
- an interior point of one edge in an L-fold parallel bundle does not disconnect the graph because L>=2.
Thus the maximum is exactly L.

## Scope

This is only a finite-stage statement. It does not settle homeomorphism or automorphism-conjugacy questions for the inverse-limit diagonal spectra, whose bonding maps contain additional information not captured by these two finite-stage invariants.

## Reproducibility

Run `artifacts/verify_counts.py`. The script checks the Euler counts and cut-point cases for 2<=L<=10 as a finite sanity check; the proof above is valid for all L>=2.

## Reference

- L. Obermeyer, W. Winter, *A C*-diagonal in the Jiang–Su algebra via entangled matrix cones*, arXiv:2607.03129.
