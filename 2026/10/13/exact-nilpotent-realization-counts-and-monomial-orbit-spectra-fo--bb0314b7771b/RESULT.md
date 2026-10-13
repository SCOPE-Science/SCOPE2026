# Exact nilpotent realization counts and monomial orbit spectra for looped directed cycles

## Finding

Write \(q=p^e\), with \(p\) prime, and \(n=hm\ge3\), where \(h=p^{v_p(n)}\) and \(p\nmid m\). For the irreducible zero–nonzero pattern consisting of a directed \(n\)-cycle plus one loop at every vertex, the number of nilpotent realizations over \(\mathbb F_q\) is

\[
N_{n,q}=\begin{cases}
\dfrac{(q-1)^n}{m}\dfrac{n!}{(h!)^m},&m\mid(q-1),\\
0,&m\nmid(q-1).
\end{cases}
\]

Every nilpotent realization has nilpotency index exactly \(n\), rather than a smaller index. More finely, nilpotent realizations split into explicit monomial-conjugacy orbits. Let \(C_n\) cyclically rotate the vertices, and let \((\mathbb F_q^\times)^n\) act by invertible diagonal similarity. Under the group \(G=(\mathbb F_q^\times)^n\rtimes C_n\), if \(m\mid(q-1)\), then for each \(d\mid n\), put

\[
F(d)=\begin{cases}
\dfrac{d!}{((hd/n)!)^m},& n/d\mid h,\\
0,&\text{otherwise},
\end{cases}
\quad
O_d=\frac{q-1}{md}\sum_{c\mid d}\mu(d/c)F(c).
\]

Exactly \(O_d\) orbits have \((q-1)^{n-1}d\) matrices; all other orbit sizes are absent. Equivalently, the total number of orbits is

\[
\frac{q-1}{mn}\sum_{j\mid h}\varphi(j)\frac{(n/j)!}{((h/j)!)^m}.
\]

For example, when \(q=4\) and \(n=6\), there are exactly \(21{,}870\) nilpotent realizations. Their monomial orbits consist of two orbits of size \(729\) and fourteen orbits of size \(1{,}458\). This is an exact symmetry refinement of the previously known existence criterion.

## Assumptions and scope

All indices are interpreted modulo \(n\). Matrices \(A\in M_n(\mathbb F_q)\) have nonzero diagonal entries \(a_i=A_{i,i}\) and nonzero cycle entries \(b_i=A_{i,i+1}\) for \(1\le i<n\) and \(b_n=A_{n,1}\); every other entry is zero. Every specified nonzero condition is mandatory, and distinct labelled matrices are counted separately. The monomial group used above is the full subgroup of invertible monomial matrices preserving this zero–nonzero pattern by conjugation: its permutation parts are precisely the cyclic rotations for \(n\ge3\). This is *not* classification up to unrestricted \(\operatorname{GL}_n(\mathbb F_q)\)-similarity.

## Proof

**1. Characteristic polynomial and diagonal roots.** Put \(B=\prod_{i=1}^n b_i\ne0\). The only nontrivial cycle permutation in the determinant expansion of \(tI-A\), apart from fixed points, is the entire directed \(n\)-cycle. Its contribution is \(-B\). Consequently,

\[
\chi_A(t)=\prod_{i=1}^n(t-a_i)-B.
\]

The nilpotence criterion \(\chi_A(t)=t^n\) is therefore precisely

\[
\prod_{i=1}^n(t-a_i)=t^n+B.\tag{1}
\]

Let \(h=p^{v_p(n)}\), \(m=n/h\), \(p\nmid m\). As the \(h\)-th power map is an automorphism of \(\mathbb F_q\), there is a unique \(\beta\ne0\) with \(\beta^h=B\). In characteristic \(p\),

\[
t^n+B=(t^m+\beta)^h.
\]

The degree-\(m\) factor is separable because its derivative is \(mt^{m-1}\) and its roots are nonzero. It splits into linear factors over \(\mathbb F_q\) precisely when \(m\mid(q-1)\) and \(-\beta\) is an \(m\)-th power. Indeed, after choosing one root \(a\ne0\), all \(m\) roots are the \(m\)-th roots of unity multiplied by \(a\); separability forces all of them to lie in the field. Conversely those conditions give exactly that splitting. Thus, for each allowed \(B\), the diagonal word consists of each of \(m\) distinct roots occurring exactly \(h\) times.

**2. Counting the labelled realizations.** When \(m\mid(q-1)\), the set of allowed nonzero values \(B=-a^n\), as \(a\) varies over \(\mathbb F_q^\times\), has size \((q-1)/m\), because \(\gcd(n,q-1)=m\). For each allowed \(B\), there are precisely \(n!/(h!)^m\) labelled diagonal words. There are independently \((q-1)^{n-1}\) ordered nonzero edge-weight tuples of product \(B\). Multiplication proves the formula for \(N_{n,q}\); if \(m\nmid(q-1)\), equation (1) has no solution and the count is zero.

**3. Nilpotency index.** Consider the vectors \(e_n,Ae_n,\ldots,A^{n-1}e_n\). For each \(0\le j<n\), the vector \(A^je_n\) has zero coordinates before \(n-j\), while its coordinate at \(n-j\) is the nonzero product \(b_{n-j}\cdots b_{n-1}\) (empty product for \(j=0\)). No traversal can wrap around the directed cycle in fewer than \(n\) steps. These vectors are therefore linearly independent. Hence \(A\) is cyclic with minimal polynomial equal to its characteristic polynomial. For a nilpotent realization this polynomial is \(t^n\), proving regular nilpotence.

**4. Diagonal similarity and rotations.** Diagonal conjugation fixes the ordered diagonal word \((a_1,\ldots,a_n)\) and product \(B\). Conversely, if those invariants agree, solve successively for nonzero diagonal conjugating coefficients along the \(n-1\) successive edges; the final edge matches automatically because the total edge products agree. Thus the diagonal torus acts transitively on each set of edge weights with a fixed product, and the effective orbit has size \((q-1)^{n-1}\) (the common scalar matrices are the kernel). A monomial conjugation can preserve the directed cycle support only by a cyclic rotation. Therefore monomial-conjugacy classes correspond exactly to cyclic rotation classes of diagonal words over the fixed \(m\)-element root set, with each root repeated \(h\) times. Different allowed products \(B\) cannot lie in the same orbit.

**5. Exact period and orbit sizes.** For any divisor \(d\mid n\), a diagonal word is fixed by rotation through \(d\) positions exactly when it is a block of length \(d\) repeated \(n/d\) times. Such a word exists precisely when \(n/d\mid h\), and then the number is \(F(d)=d!/((hd/n)!)^m\). If \(E(d)\) counts words with *least* positive rotation period exactly \(d\), then \(F(d)=\sum_{c\mid d}E(c)\). Möbius inversion yields \(E(d)=\sum_{c\mid d}\mu(d/c)F(c)\). A cyclic class of least period \(d\) contains exactly \(d\) words; each word contributes its \((q-1)^{n-1}\)-element diagonal-similarity fiber. Hence each such monomial orbit has size \((q-1)^{n-1}d\), and multiplying \(E(d)/d\) by the \((q-1)/m\) allowed choices of \(B\) gives exactly \(O_d\). Burnside's lemma for the rotations gives the stated total-orbit formula, with a rotation of order \(j\) fixing \((n/j)!/((h/j)!)^m\) words when \(j\mid h\). This completes the count and classification.

## Verification

The standalone `verify.py` uses explicit arithmetic tables for prime and extension finite fields; enumerates every nonzero diagonal word and permitted cycle product for the listed test cases; independently checks nilpotence by matrix powers and index \(n\); computes orbit representatives by cyclic rotation; and checks each complete orbit-size distribution against the theorem. It prints `VERIFY_OK` only when all equalities and nilpotency checks pass.

The cases include \(q=2,3,4,5,7,9\), various \(n\) from \(3\) through \(6\), both vanishing and nonvanishing strata, and inseparable examples in characteristics \(2\) and \(3\). In particular, the complete \((q,n)=(4,6)\) count and period spectrum are reproduced. These finite checks are not a proof for unbounded \(n\) or \(q\); the proof above supplies the general argument.

## Relationship to prior work

Vander Meulen and Van Tuyl (2009), Theorem 4.6, **already proves the exact existence criterion** for this very directed-cycle-with-all-loops pattern over arbitrary fields: existence is equivalent to splitting of the relevant roots-of-unity polynomial. The present finding does not claim that existence criterion as new. Rather, it gives the full labelled finite-field multiplicity, nilpotency-index assertion, and *every orbit size and multiplicity* under the natural pattern-preserving monomial group, including the inseparable parameter range. Their Section 5 classifies existence for small prime fields, but does not give these quantitative orbit formulas. Campbell, Vander Meulen, and Van Tuyl (2011) develop further pattern-existence constructions and roots-of-unity criteria; these do not imply the explicit counts recorded here without new enumeration. Engel and Schneider (1982), Theorems 3.8 and Corollary 3.9, provide general diagonal-similarity canonical forms, which underpin the equivalence of fixed cycle-product data; this classical ingredient is not new. The finite-field splitting, diagonal-word multiplicities, and rotational stabilizer distribution are combined for the precise nilpotent-support stratum treated here.

## Limitations

The statement concerns a single irreducible support family and is not a general classification of potentially nilpotent zero–nonzero patterns. It counts labelled matrices and pattern-preserving monomial-similarity classes, not all similarity classes; all nilpotent realizations are in fact one unrestricted regular-nilpotent similarity class. The component arguments are elementary and closely tied to established root-of-unity and diagonal-similarity facts. Although searches of the most relevant sources revealed no previously published quantitative monomial-orbit spectrum for this pattern, an equivalent formulation in unindexed enumeration or matrix-pattern literature remains possible. No independent priority or mathematical audit is claimed.

## References

1. K. N. Vander Meulen and A. Van Tuyl, *Zero-nonzero patterns for nilpotent matrices over finite fields*, Electronic Journal of Linear Algebra **18** (2009), 628–648, Theorem 4.6 and Section 5. arXiv:0812.0527, DOI:10.13001/1081-3810.1335; https://journals.uwyo.edu/index.php/ela/article/download/671/671/671
2. N. Campbell, K. N. Vander Meulen, and A. Van Tuyl, *Structure of nilpotent matrices over fields*, Electronic Journal of Linear Algebra **22** (2011), 931–958, Sections 2 and 4. DOI:10.13001/1081-3810.1483; https://journals.uwyo.edu/index.php/ela/article/download/967/967/967
3. G. M. Engel and H. Schneider, *Algorithms for testing the diagonal similarity of matrices and related problems*, SIAM Journal on Algebraic and Discrete Methods **3** (1982), 429–438, Theorem 3.8 and Corollary 3.9. DOI:10.1137/0603044; https://people.math.wisc.edu/hans/paper_archive/scanned_papers/hs066.pdf
