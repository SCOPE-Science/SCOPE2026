# Five degree strata in the comaximal graph of the five-dimensional Heisenberg Lie algebra

## Finding
Let \(q\) be any prime power and let \(L=H_5(\mathbb F_q)\) have basis \(x_1,y_1,x_2,y_2,z\), nonzero brackets \([x_1,y_1]=[x_2,y_2]=z\), and central \(z\). In the comaximal graph \(\Gamma(L)\), vertices are all nonzero proper Lie subalgebras and different vertices are adjacent when they generate \(L\). The **entire degree distribution** has five distinct strata:

| Vertex type | Multiplicity | Degree |
| --- | ---: | ---: |
| Central line \(\mathbb F_qz\) | \(1\) | \(0\) |
| Subalgebras with one-dimensional image in \(L/\mathbb F_qz\) | \((q^3+q^2+q+1)(q+1)\) | \(q^3\) |
| Two-dimensional *isotropic* image | \((q^2+1)^2(q+1)\) | \(q^5+q^4+q^3+q^2\) |
| Two-dimensional *nondegenerate* image | \(q^2(q^2+1)\) | \(q^5+q^4+q^2\) |
| Three-dimensional image | \(q^3+q^2+q+1\) | \(q^5+3q^4+3q^3+2q^2+q\) |

In particular, the graph has \(1+(q^3+q^2+q+1)(q+2)+(q^2+1)^2(q+1)+q^2(q^2+1)\) vertices, and this table specifies their degrees including the unique isolated vertex.

## Assumptions and scope
The quotient \(V=L/\mathbb F_qz\) is a symplectic four-space with alternating nondegenerate form \(\omega\) given by the displayed brackets. Isotropic two-planes are precisely Lagrangian planes; nondegenerate means the restricted alternating form has rank two. All fields \(\mathbb F_q\), including even characteristic, are included. Counts concern actual subalgebras, not conjugacy classes. No claim about other five-dimensional Lie algebras or higher Heisenberg dimensions is made.

## Proof
Write \(\pi:L\to V\) for the quotient. Any subalgebra \(U\) with image \(S\le V\) either contains \(z\), when \(U=\pi^{-1}(S)\), or does not contain \(z\), when \(U\) is the graph of a linear functional \(S\to\mathbb F_q\). Such a graph is bracket-closed exactly when \(S\) is isotropic. Therefore the fiber of the projection map from subalgebras to subspaces of \(V\) has size \(1+q^{\dim S}\) for isotropic \(S\), and size \(1\) otherwise. The excluded case \(S=V\) gives the whole algebra; \(S=0\) supplies the single central-line vertex.

For proper subalgebras \(U,W\), generation of \(L\) is equivalent to \(\pi(U)+\pi(W)=V\). Indeed, when the images span \(V\), the generated Lie subalgebra contains brackets spanning \(\mathbb F_qz\), since \(\omega\) is nondegenerate, and hence is all of \(L\). Conversely, a proper subspace of \(V\) containing both images prevents generation. Thus adjacency is the spanning relation on projected subspaces, with the above fiber multiplicities.

The numbers of lines and hyperplanes of \(V\) are both \(h=q^3+q^2+q+1\). Every line is isotropic and has \(q+1\) subalgebras above it; every hyperplane has nonzero restricted form and only its full preimage is a subalgebra. The number of isotropic planes is \(i=(q^2+1)(q+1)\): every projective line lies in exactly \(q+1\) Lagrangian planes, while every Lagrangian plane contains exactly \(q+1\) projective lines. Counting incidences gives \(i=h=(q^2+1)(q+1)\). The total number of planes is \((q^2+1)(q^2+q+1)\), leaving \(q^2(q^2+1)\) nondegenerate planes. Isotropic planes have fiber weight \(q^2+1\), nondegenerate planes weight \(1\).

A line is complementary only to hyperplane images not containing it. Of the \(h\) hyperplanes, \(q^2+q+1\) contain a given line, giving degree \(q^3\). A fixed plane \(S\) has \(q^3+q^2\) hyperplanes not containing it. It has exactly \(q^4\) complementary planes (graphs over any fixed complement). When \(S\) is isotropic, precisely \(q^3\) complementary planes are isotropic, parametrized by symmetric bilinear forms on a two-space. Its weighted complementary-plane count is \(q^3(q^2+1)+(q^4-q^3)=q^5+q^4\). When \(S\) is nondegenerate, take its symplectic orthogonal complement. A graph plane is isotropic exactly when the corresponding two-by-two linear map has a specified nonzero determinant. There are \(|\mathrm{SL}_2(\mathbb F_q)|=q(q^2-1)\) such maps, giving weighted complementary-plane count \(q(q^2-1)(q^2+1)+(q^4-q(q^2-1))=q^5+q^4-q^3\). Adding the hyperplane contribution gives the two plane degrees in the table.

Fix a hyperplane \(H\le V\). There are \(h-1=q^3+q^2+q\) other hyperplane vertices and \(q^3(q+1)=q^4+q^3\) line vertices outside \(H\). Among the \(q^2+q+1\) planes contained in \(H\), precisely \(q+1\) are isotropic: they are the planes through the one-dimensional radical of \(\omega|_H\). Hence the total weighted number of planes contained in \(H\) is \((q+1)(q^2+1)+q^2=q^3+2q^2+q+1\). The total plane-fiber weight is \((q^2+1)(q^3+2q^2+q+1)\); subtracting the contained weight yields \(q^2(q^3+2q^2+q+1)\). Summing the three contributions gives \(q^5+3q^4+3q^3+2q^2+q\). The central line has image zero and is isolated. All multiplicities follow from the fiber counts, completing the degree census.

## Verification
Run \(\texttt{python verify.py}\) using Python 3 with no third-party dependencies. The program enumerates every reduced-row-echelon subspace of \(\mathbb F_p^5\) for \(p=2,3\), tests closure under the displayed bracket independently of the symbolic fiber classification, builds the full comaximal adjacency matrix through quotient rank, and compares degree/multiplicity histograms. It checks 156 vertices for \(p=2\) and 691 for \(p=3\). The general prime-power theorem comes from the proof, not these finite tests.

## Relationship to prior work
Towers, Zuleta, and Gutierrez (arXiv:2605.09583v1, May 10, 2026) introduce this graph and classify Lie algebras of dimension at most three; their detailed graph results do not cover \(H_5\). Their later arXiv:2608.16575v1 (August 17, 2026) explicitly advertises additional dimension-four families, but an accessible complete text was not available to compare every proposition. Results on the subalgebra commutativity degree of Heisenberg Lie algebras instead count commuting pairs of subalgebras and do not supply these generation-graph vertex degrees. The present census uses symplectic isotropic/nondegenerate plane fibers, which have no analogue in dimension three.

## Limitations
This proof and its computational checks have not received an independent audit or historical uniqueness certification. The August follow-up was compared through its abstract rather than complete text; a different older graph formulation could overlap. The proof assumes finite fields and exactly five-dimensional Heisenberg algebra, and does not assert generalization to higher rank.

## References
- D. A. Towers, Y. Zuleta, I. Gutierrez, *The comaximal graph of a finite-dimensional Lie algebra*, arXiv:2605.09583v1 (2026-05-10), https://arxiv.org/abs/2605.09583.
- D. Towers, Y. Zuleta, I. Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575v1 (2026-08-17), https://arxiv.org/abs/2608.16575.
