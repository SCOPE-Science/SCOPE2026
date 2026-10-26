# Review of the exact characteristic-eleven Cartier intersection

## Correctness — PASS
The genus-two smoothness condition is exactly \(v(u^2-4v)(1-u+v)\ne0\). The parity of the sextic kills both off-diagonal Cartier coefficients, and coefficient extraction yields the explicit pair \(A,B\). The resultant factorization has eight simple projected roots outside \(u=2\); on \(u=2\) the fiber has three distinct support points, two with Jacobian determinant \(8\). The local resultant order \(17\) leaves length \(15\) at the degenerate \((2,1)\). The absence of points at infinity and the boundary gcds establish geometric completeness. `verify.py` recomputes the exact characteristic-eleven identities, with no sampling substituted for proof.

## Originality — PASS with residual risk
The same even sextic is a published normal form, including in Ohashi's arXiv:2308.11963, Lemma 3.3. Harashita–Yamamoto arXiv:2409.13212 prove a more general smooth Rosenhain multiplicity-one theorem, so reducedness alone is not claimed to be new. Katsura–Takashima arXiv:2003.00633, Section 7.2, explicitly identify **two** isomorphism classes in characteristic eleven, a different invariant from the **ten** marked parameters. The inspected results do not present the exact \(10+15\) affine Cartier intersection in these coordinates. Uninspected alternate coordinates or earlier tables remain an originality risk.

## Mathematical value — PASS
This resolves a natural, fully defined intersection problem on a two-parameter moduli cover, distinguishing its ten legitimate smooth points from a concentrated length-fifteen degeneration of the coefficient equations. The boundary excess is mathematically meaningful: without it an affine Bézout count of twenty-five would misleadingly suggest twenty-five valid superspecial curves. The finite computation is motivated by the geometry of superspecial curves and marked involutions, not an arbitrary slice.

## Limits
No new classification of abstract isomorphism classes is claimed, nor is the boundary scheme identified with a singular Jacobian. Literature search cannot certify absence of equivalent old formulas. Independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
