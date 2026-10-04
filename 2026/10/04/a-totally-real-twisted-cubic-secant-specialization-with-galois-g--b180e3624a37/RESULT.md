# A totally real twisted-cubic secant specialization with Galois group \(S_{10}\)
## Finding
For the exact rational matrix of Example 2.4 in Aslam–Faust–Hauenstein–Lopez Garcia–Kagy–Regan–Wampler–Zhang, let \(u=t_1+t_2\) on each of the ten common-secant orbits of the standard twisted cubic and its image. The ten \(u\)-values are the roots of the explicit primitive degree-10 elimination polynomial recorded in the verification package, and that polynomial has splitting-field Galois group \(S_{10}\) over \(\mathbb{Q}\). Since the source independently certifies that all ten common secants for this exact matrix are totally real, this gives an explicit rational specialization that is simultaneously totally real and arithmetically full-symmetric.

The coefficient vector below is ordered from degree 10 down to degree 0. Thus, if it is denoted by \(c_0,\ldots,c_{10}\), then \(P(u)=\sum_{j=0}^{10}c_j u^{10-j}\).

```text
[4097057871858200718399710457050029783860448093883227674718933457227000000000000, 886550574980216626763495644940579931850647416367114988341240632505000000000000, -14583445523408363563043807155529990819517874422341082510349311651322000000000000, -5275699128677051945839235006808320077582295289599096827353598942811453300000000, 17554592606358550297152133225066058371683785754779718519967513497275130300000000, 8606156808171959940381182770903055017106302150492576001858996085131852000000000, -6999255125012068183983935339635630280233270657536727356116586004108299033030000, -4299485645818848556385308962411578844253286727339888981739646169646110507450000, -143456610277323149419672668802489602321319249963404595109173337004241260620000, 4519935476335806902498900300573315260877836169182856532548525582293189114273, 30338654869700262466652210847156386094220876251571377982129917845522862489]
```

## Assumptions and scope
The two curves are the standard twisted cubic \(C_0\subset\mathbf{P}^3\) and \(C_1=M C_0\), where the entries of the matrix printed as decimals in Example 2.4 are taken exactly, as stipulated there: \(1.4351=14351/10000\), and similarly for the other entries. The finding concerns the arithmetic Galois group of the ten secant orbits for this one exact specialization. It does not assert that every totally real specialization has Galois group \(S_{10}\), nor does it strengthen the paper's generic monodromy theorem.

## Proof
Write \(p_i(s)=m_{i1}+m_{i2}s+m_{i3}s^2+m_{i4}s^3\), and use the symmetric coordinates \(u=t_1+t_2\) and \(v=t_1t_2\) on an unordered pair of points of \(C_0\). The four secant equations from the source say that \(s_1\) and \(s_2\) are common roots of
\[
A(s)=p_3(s)-u p_2(s)+v p_1(s),
\]
\[
B(s)=p_4(s)-(u^2-v)p_2(s)+uv p_1(s).
\]
For a genuine common secant with \(s_1\ne s_2\), these two cubics share a quadratic factor. The exact derivation in `derive_elimination.py` computes their subresultant sequence, sets both coefficients of the degree-one subresultant equal to zero, eliminates \(v\), and extracts the unique degree-10 factor. After primitive integer normalization this is exactly the polynomial \(P\) recorded above. The same derivation checks that \(M\) is invertible and that the only other factor in this symmetric elimination is \((77238u-51509)^3\), coming from the leading-coefficient degeneration \(u=51509/77238\). The ten representatives printed in Example 2.4 have pairwise distinct sums \(t_1+t_2\); even using only the four-decimal values printed there, all ten sums are separated from \(51509/77238\). Hence all ten genuine secant-orbit \(u\)-values lie on the degree-10 factor \(P\), and degree counting shows they are exactly its ten roots.

Now reduce \(P\) modulo 19. After monic normalization it is irreducible of degree 10. Therefore \(P\) is irreducible over \(\mathbb{Q}\), and the arithmetic Galois group \(G\le S_{10}\) is transitive. The squarefree factorization modulo 19 also supplies a Frobenius element that is a 10-cycle.

Modulo 17, the monic reduction factors as an irreducible cubic times an irreducible septic. Hence a Frobenius element has cycle type \((7)(3)\); its cube is a 7-cycle. A transitive subgroup of \(S_{10}\) containing a 7-cycle is primitive: any nontrivial block system would have blocks of size 2 or 5, but the 7-cycle induces the identity on the corresponding set of 5 or 2 blocks and therefore would have to preserve each block, impossible for its 7-point orbit. Jordan's theorem then gives \(A_{10}\le G\), because \(7\le 10-3\). Finally, the 10-cycle is odd, so \(G\not\subseteq A_{10}\). Thus \(G=S_{10}\).

The source's Example 2.4 independently certifies, for this exact matrix, 40 real isolated ordered solutions grouped into ten four-element swapping orbits, so all ten corresponding common secants are totally real. Combining that certified reality statement with the arithmetic computation proves the finding.

## Verification
Run `python derive_elimination.py` with SymPy available. It reconstructs the degree-10 factor directly from the exact matrix and secant equations and prints `ELIMINATION_OK`. Run `python verify_galois.py`; this second checker uses only the Python standard library, verifies irreducibility modulo 19 by Rabin's criterion, verifies the explicit irreducible degree-3 and degree-7 factorization modulo 17, and prints `VERIFY_OK`. The captured outputs are included as `derive_output.txt` and `verify_output.txt`.

## Relationship to prior work
Aslam et al. prove that the geometric monodromy group of the ten common secants over the complex parameter space is \(S_{10}\), and their Example 2.4 supplies the exact rational matrix and certifies that its ten common secants are totally real. Their theorem concerns monodromy of the moving family; it does not state the arithmetic Galois group of the fixed Example 2.4 specialization. The accompanying repository contains the certified monodromy loops and the same base point, but no fixed-fiber degree-10 elimination polynomial or arithmetic Galois certificate was found there. Targeted database and web searches likewise found the paper and generic-monodromy discussions, but no source asserting this specialization-level \(S_{10}\) result.

## Limitations
The novelty comparison is literature-based rather than a proof of absence from all unpublished work. The result is specific to the exact rational Example 2.4 matrix. Jordan's theorem and the Frobenius cycle-type criterion are standard group- and Galois-theoretic inputs. The source, not this package, supplies the independent certification that the ten secants are totally real; the new package supplies the exact elimination and arithmetic Galois certificate.

## References
1. S. Aslam, M. Faust, J. D. Hauenstein, J. Lopez Garcia, B. Kagy, M. H. Regan, C. W. Wampler, A. Zhang, *Common Real Secants to Pairs of Real Twisted Cubic Curves*, arXiv:2603.25003v1, 26 March 2026.
2. Companion repository, `mattfaust/SecantsofTwoCubicsMRC2025`, especially `README.md` and `Monodromy_computation.txt`.
3. J. D. Dixon and B. Mortimer, *Permutation Groups*, Springer, 1996, discussion of Jordan's theorem for primitive permutation groups.
