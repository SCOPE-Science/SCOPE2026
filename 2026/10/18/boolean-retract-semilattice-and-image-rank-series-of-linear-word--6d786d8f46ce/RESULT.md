# Boolean retract semilattice and image-rank series of linear-word flat semirings

## Finding
For every integer \(m\ge1\), all idempotent endomorphisms of the finite linear-word flat semiring \(A_m\) are exactly the letter-deletion maps \(P_S\), indexed by subsets \(S\subseteq\{1,\ldots,m\}\). They satisfy \(P_SP_T=P_{S\cap T}\); thus the idempotents of the endomorphism monoid form the Boolean meet-semilattice on \(m\) letters and number exactly \(2^m\). The generating function for the number of these retracts by nonzero image size is
\[
\sum_{m\ge0}\left(\sum_{P\in\operatorname{End}(A_m),\ P^2=P} z^{|\operatorname{im}P|-1}\right)t^m
=\frac{1+B(t,z)}{1-t-tB(t,z)},\qquad
B(t,z)=\sum_{\ell\ge1}t^\ell z^{\ell(\ell+1)/2}.
\]
In particular, for the eleven-element semiring \(A_4\), its retract-rank polynomial is
\[
1+4z+3z^2+3z^3+2z^4+2z^6+z^{10}.
\]

## Assumptions and scope
Let \(A_m\) have the absorbing element \(0\) and nonzero elements \([i,j]\) for integers \(1\le i\le j\le m\). The operations are
\[
x+y=\begin{cases}x,&x=y,\\0,&x\ne y,\end{cases}
\qquad
[i,j]\,[k,\ell]=\begin{cases}[i,\ell],&k=j+1,\\0,&k\ne j+1.\end{cases}
\]
The element \(0\) is absorbing for multiplication. It is also the top/absorbing value for addition, not an additive identity. A semiring endomorphism preserves both binary operations; preservation of \(0\) follows automatically from them. We use idempotent **endomorphism** to mean \(P\circ P=P\), not a multiplicatively idempotent element. Put \(a_i=[i,i]\).

For each \(S\subseteq\{1,\ldots,m\}\), define \(P_S(0)=0\) and
\[
P_S([i,j])=\begin{cases}[i,j],&\{i,i+1,\ldots,j\}\subseteq S,\\0,&\text{otherwise.}\end{cases}
\]
Set \(\rho(P)=|\operatorname{im}P|-1\), counting nonzero image elements. The \(m=0\) coefficient in the generating function uses the one-element semiring and its unique map, only as a combinatorial convention.

## Proof
**Step 1 (zero and separation).** Every nonzero element of \(A_m\) squares to \(0\), whereas \(0^2=0\), so \(0\) is the unique multiplicatively idempotent element. Hence any endomorphism \(P\) sends \(0\) to \(0\). For distinct \(x,y\) with \(P(x)=P(y)=v\ne0\), preservation of flat addition would give
\[
0=P(x+y)=P(x)+P(y)=v,
\]
a contradiction. Thus no two distinct elements have the same nonzero image.

**Step 2 (idempotence forces partial identity).** If \(P^2=P\) and \(P(x)=v\ne0\), then \(P(v)=v\). Step 1 applied to \(x,v\) therefore forces \(x=v\). Consequently every element is either fixed or sent to zero. Let \(S=\{i:P(a_i)=a_i\}\). The factorization \([i,j]=a_i a_{i+1}\cdots a_j\) now implies that \(P([i,j])=[i,j]\) exactly when every index between \(i\) and \(j\) lies in \(S\), and that \(P([i,j])=0\) otherwise. Hence \(P=P_S\). Conversely, the displayed rule for \(P_S\) preserves flat addition (its nonzero images are pairwise distinct), preserves multiplication (concatenation survives exactly when every constituent letter survives), and is idempotent. Different subsets give different images on the letters. Moreover \(P_SP_T=P_{S\cap T}\), establishing the Boolean meet-semilattice description.

**Step 3 (all retract ranks).** The nonzero image elements for \(P_S\) are exactly intervals contained in \(S\). If the maximal consecutive runs in \(S\) have lengths \(\ell_1,\ldots,\ell_r\), then each run of length \(\ell\) contributes exactly \(\ell(\ell+1)/2\) intervals, and
\[
\rho(P_S)=\sum_{j=1}^r\frac{\ell_j(\ell_j+1)}2.
\]
Every binary word of length \(m\) encodes one \(S\). Let \(B(t,z)=\sum_{\ell\ge1}z^{\ell(\ell+1)/2}t^\ell\), the weight of one nonempty run of selected letters. Binary words containing no selected letters have generating function \(1/(1-t)\). Words with at least one selected run consist of arbitrary initial zeroes, a selected run, any number of additional selected runs separated from the preceding run by a nonempty zero block, and arbitrary trailing zeroes. Their series is
\[
\frac{B}{(1-t)^2}\frac1{1-\frac{tB}{1-t}}.
\]
Adding the all-zero contribution simplifies to \((1+B)/(1-t-tB)\), completing the proof. The coefficient computation at \(m=4\) gives the displayed rank polynomial. Substituting \(z=1\) yields \(1/(1-2t)\), independently verifying the total \(2^m\).

## Verification
The standalone Python 3 program `verify.py` constructs the operation tables independently and checks all possible generator-image assignments for \(1\le m\le4\). There are respectively \(2\), \(12\), \(148\), and \(3320\) endomorphisms; respectively \(2\), \(4\), \(8\), and \(16\) are idempotent. The program checks both operations on every ordered element pair, idempotence by composition, equality with all predicted letter-deletion maps, and the run-length polynomial recurrence. Execute `python verify.py` with no external dependencies. These exhaustive finite checks test examples; the unrestricted theorem follows from Steps 1–3, not from computational extrapolation.

## Relationship to prior work
The interval semirings \(A_m\) are the canonical finite generators appearing in A. Wang and L. Wang's 2026 investigation of finite identity bases for flat semirings of linear words [1]. Gao, Ren and Zhao earlier studied finite basability for related flat word semirings [2]. Their accessible abstracts concern identity bases and varieties, while the theorem here concerns idempotents in an endomorphism monoid, all retract images, and their exact image-rank distribution; an identity-basis theorem alone does not imply those enumerations. The complete text of [1] could not be inspected, so this comparison does not claim verified full-document noncoverage.

## Limitations
This classifies only idempotent endomorphisms, not arbitrary endomorphisms or the full endomorphism monoid multiplication. The generating series is a formal power series in \(t\) with polynomial coefficients in \(z\). The claim makes no assertion about semirings defined by nonlinear words, commutative-factor variants, or multiset-valued additions. Prior-art novelty remains conditional on incomplete full-text coverage and on the absence of unknown equivalent formulations; no independent mathematical audit has been performed.

## References
[1] Aifa Wang and Lili Wang, *Finite identity bases for flat semirings of linear words*, arXiv:2609.14349, first submitted September 13, 2026, https://arxiv.org/abs/2609.14349.

[2] Zidong Gao, Miaomiao Ren, and Xianzhong Zhao, *The finite basis problem for the flat semirings \(S(W)\)*, arXiv:2608.12284, first submitted August 2026, https://arxiv.org/abs/2608.12284.
