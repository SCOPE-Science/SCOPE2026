# Independent mathematical audit — SCOPE-20260920-a555a8810a2a

Final disposition: **PASS**.

## Correctness
**PASS** — For binary cube vertices, \((x-y)\cdot(z-y)\) equals the number of coordinates with \(x_i=z_i\ne y_i\), so cubic acuteness is exactly the hypercube general-position condition. The complete C++ verifier was inspected: for every deletion set of size \(0\) through \(7\), it enumerates all \(2^{11}\) candidate vertices individually compatible with every retained base pair, then exhaustively backtracks over the required \(r+1\) new vertices while checking every new-new-retained triple and every all-new triple. Removed base vertices are allowed to reappear, so no completion type is omitted. An independent compile-and-run reproduced the recorded counts and `NONE` result at every radius. Thus any size-25 general-position set sharing at least 17 vertices with the displayed 24-set would have appeared and is excluded.

## Originality
**PASS** — The Kamenetsky/OEIS source supplies the 24-point \(Q_{11}\) witness, and Korže-Vesel's complete open article gives the hypercube/general-position to \((2,1)\)-separating formulation and computational lower-bound context. Neither supplies a local exchange-isolation theorem. Searches under cubic acute, hypercube general position, \((2,1)\)-separating systems, frameproof codes, exchange neighborhoods, overlap, and maximality located no prior result forcing symmetric difference at least 17 from this witness. Originality therefore passes to the best of current knowledge.

### Equivalent formulations
All major aliases were searched and the computational theorem was tied to the actual published witness.

### Broader coverage
No inspected broader theorem implies the seven-exchange isolation statement.

### Exact database or table
The exact external table establishes the witness and motivation, not the new local obstruction.

### Claim versus prior implication
The claim is not a corollary of the inspected coding/geometric results.

## Value
**PASS** — The result gives an exact, symmetry-stable local obstruction around the strongest recorded 24-point \(Q_{11}\) witness: any one-point improvement must replace at least eight old vertices and introduce at least nine new ones. That is a meaningful finite structural cutoff for an unresolved extremal search, not an arbitrary enumeration.

## Source inspections
- **Lower bounds and their solutions for a(11-15)** (https://oeis.org/A089676/a089676_1.txt): complete attachment containing the \(a(11)\ge24\) vector list Method: primary construction record inspection. Assessment: WITNESS_SOURCE_NOT_LOCAL_ISOLATION. Evidence: The 24 displayed vectors agree with the audited base configuration but no exchange-radius theorem is stated.
- **General Position Sets in Two Families of Cartesian Product Graphs** (https://doi.org/10.1007/s00009-023-02416-z): complete open web article, including the hypercube section and SAT formulation Method: primary open full-text inspection. Assessment: GLOBAL_HYPERCUBE_CONTEXT_NOT_LOCAL_COVERAGE. Evidence: The article develops lower-bound/exact computations for hypercubes but does not state an overlap or exchange-isolation result for the \(Q_{11}\) witness.
- **Assigned exhaustive verifier** (repository artifact `artifacts/verify_exchange.cpp`): complete C++ source and recorded output, followed by an independent compile-and-run Method: repository artifact inspection and replay. Assessment: EXHAUSTIVE_CERTIFICATE_RECONSTRUCTED. Evidence: Every deletion radius through seven and every compatible completion is enumerated; the replay reproduced all recorded counts and found no size-25 completion.

## Checked sources
- https://oeis.org/A089676/a089676_1.txt
- https://doi.org/10.1007/s00009-023-02416-z
- repository artifact `artifacts/verify_exchange.cpp`

## Residual risks
- Equivalent local-stability results could exist under frameproof-code or separating-system terminology not found in the searches.
- The theorem is local to the displayed witness and its cube automorphisms; it does not prove \(gp(Q_{11})=24\).
