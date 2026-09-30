# Independent Audit — 2026/09/12/028

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `58d6ac1011d62c1ff43c35cade8bb291e663e33f`  
**Disposition:** **PASSED**

## Correctness

The Lovasz-theta lower-bound certificate checks exactly. Using rational arithmetic, the 35x35 matrix B is symmetric, has trace 1, has B_ij=0 on all 248 graph edges, and has objective <J,B>=754549/100000. The supplied rational LDL^T factorization reconstructs every entry of B exactly and all 35 pivots are positive, hence B is positive definite and therefore feasible for the standard primal SDP theta(G)=max <J,X> subject to Tr(X)=1, X_ij=0 on edges, X>=0. Consequently theta(G35)>=7.54549 is rigorously certified.

## Originality

Exoo’s 2012 paper and McKay’s Ramsey-graph database establish and distribute the 35-vertex Ramsey(4,6) witnesses but do not tabulate Lovasz-theta values or an exact SDP certificate for the first graph. Targeted searches for the graph6 corpus together with Lovasz theta found no prior source stating the exact 7.54549 lower bound or an equivalent rational certificate. The submitted claim is not implied by the Ramsey property alone.

## Scientific value

A rigorous semidefinite invariant of a canonical extremal Ramsey witness is useful independently of the witness’s prior discovery. The exact rational certificate converts a floating-point optimization observation into a portable, verifier-independent lower bound and quantifies a substantial gap between the graph’s independence number (at most 5) and its theta relaxation. This is a nontrivial exact invariant of a natural frontier object.

## Limitations

- The certificate proves only the lower bound theta(G35)>=7.54549, not the exact theta value.
- The audit verifies the first pinned witness only and makes no assertion about the other 36 known Ramsey(4,6;35) graphs.
- Originality searches found no prior theta tabulation, but absence of a search hit is not a proof that no unpublished computation exists.

## Evidence

- [Geoffrey Exoo, On the Ramsey Number R(4,6)](https://doi.org/10.37236/2102): Establishes the 37 Ramsey(4,6;35) witnesses and their Ramsey role, without reporting Lovasz-theta data.
- [Brendan McKay, Ramsey Graphs](https://users.cecs.anu.edu.au/~bdm/data/ramsey.html): Distributes r46_35some.g6 and records the witness corpus; no theta invariant is listed.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `58d6ac1011d62c1ff43c35cade8bb291e663e33f`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
