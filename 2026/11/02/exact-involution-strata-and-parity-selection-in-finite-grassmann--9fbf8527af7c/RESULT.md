# Exact involution strata and parity selection in finite Grassmann automorphism groups

## Finding
Let \(q\) be an odd prime power and \(n\ge2\). Write \(E_n=\Lambda_{\mathbb F_q}(\mathbb F_q^n)\) for the full finite exterior algebra. For \(0\le b\le n\), let \(I_{n,b}(q)\) count algebra automorphisms \(\sigma\) with \(\sigma^2=1\) whose induced map on the augmentation quotient \(J/J^2\) has negative-one eigenspace of dimension \(b\). Put \(a=n-b\), \(h=2^{n-1}\), and
\[
 O_+(n,b)=\begin{cases}h&b=0,\\0&b=n,\\2^{n-2}&0<b<n,\end{cases}\qquad O_-(n,b)=h-O_+(n,b).
\]
Define
\[
 u_n=(n+1)h-n^2-\mathbf1_{n\text{ odd}},\qquad
 f_{n,b}=O_+(n,b)-\mathbf1_{n\text{ odd},\,b\text{ even}}+a(O_+(n,b)-a)+b(O_-(n,b)-b).
\]
The exact answer is
\[
 \boxed{I_{n,b}(q)={n\brack b}_q\,q^{b(n-b)+u_n-f_{n,b}}.}
\]
In particular, the number of \(\mathbb Z/2\mathbb Z\)-gradings of this algebra **as actual ordered pairs of grading subspaces**, including the trivial grading, is \(\sum_{b=0}^n I_{n,b}(q)\). Exactly \(n+1\) gradings arise up to algebra isomorphism. The sum is over actual order-dividing-two automorphisms, not over orbits. For fixed \(n\), as \(q\to\infty\) through odd prime powers, the distribution of \(b\) under a uniformly sampled such automorphism converges to the uniform distribution on \(\{1,\ldots,n-1\}\) when \(n\) is even, and on \(\{2,4,\ldots,n-1\}\) when \(n\) is odd (necessarily \(n\ge3\)). All other types have limiting frequency zero.

## Assumptions and scope
The coefficient field has odd characteristic. The algebra is the complete exterior algebra on \(n\ge2\) generators, including its identity; automorphisms are unital \(\mathbb F_q\)-algebra automorphisms. The augmentation ideal \(J\) is the unique maximal ideal, so its quotient \(J/J^2\) is invariant. Involutions include the identity. The Gaussian binomial coefficient \({n\brack b}_q\) counts \(b\)-subspaces of an \(n\)-space over \(\mathbb F_q\). All enumerated objects are distinct maps or distinct gradings, rather than similarity classes. The result makes no statement about characteristic two or infinite-dimensional Grassmann algebras.

## Proof
Set \(V=J/J^2\). The structural decomposition of automorphisms of a finite Grassmann algebra in characteristic different from two (Bavula, Theorem 2.14 and Corollary 2.15) gives
\[
 \operatorname{Aut}(E_n)=U\rtimes\operatorname{GL}(V),\qquad U=\Omega\rtimes\Gamma.
\]
Here \(\Omega\) is the group of inner automorphisms parametrized additively by odd exterior elements modulo the odd part of the center, and \(\Gamma\) is the group of parity-preserving substitutions \(x_i\mapsto x_i+w_i\), with each \(w_i\) of odd degree at least three. The parameter map \(\Gamma\to W^n\) is bijective as a set, where \(W=\bigoplus_{j\ge3,\,j\text{ odd}}\Lambda^j(V)\). Consequently
\[
 |\Omega|=q^{h-\mathbf1_{n\text{ odd}}},\quad |\Gamma|=q^{n(h-n)},\quad |U|=q^{u_n}.
\]
This decomposition is valid over all odd-characteristic finite fields: it requires only a reduced coefficient ring in which two is invertible. It does **not** assert that \(\Gamma\) is an additive group; only its set of coordinates is used to count fixed points.

Fix a linear involution \(L\in\mathrm{GL}(V)\), with positive eigenspace dimension \(a\) and negative eigenspace dimension \(b\). Conjugation by \(L\) preserves \(\Omega\) and \(\Gamma\). On the parameters of \(\Omega\), it is the natural action on \(\Lambda^{\mathrm{odd}}V\), modulo the one-dimensional central top exterior power exactly when \(n\) is odd. On the parameters of \(\Gamma\), conjugation is the linear action on \(\operatorname{Hom}(V,W)\). The dimension of the \(+1\)-eigenspace on \(\Lambda^{\mathrm{odd}}V\) is \(O_+(n,b)\): for mixed signs the trace vanishes by the identity
\[
 \operatorname{tr}(L\mid\Lambda^{\mathrm{odd}}V)=\frac{\prod_i(1+\lambda_i)-\prod_i(1-\lambda_i)}2=0,
\]
while when every sign is positive/negative, the action on all odd monomials is positive/negative. Therefore the \(+1\)-eigenspace dimensions on \(W\) and the \(-1\)-eigenspace dimensions on \(W\) are respectively \(O_+-a\) and \(O_--b\). A fixed parameter in \(\operatorname{Hom}(V,W)\) must preserve eigenspaces, giving \(a(O_+-a)+b(O_--b)\) free coordinates. Removing the odd central top element when present yields
\[
 |C_{\Omega}(L)|=q^{O_+-\mathbf1_{n\text{ odd},\,b\text{ even}}},\quad
 |C_{\Gamma}(L)|=q^{a(O_+-a)+b(O_--b)}.
\]
Uniqueness of the \(\Omega\Gamma\) factorization implies \(|C_U(L)|=q^{f_{n,b}}\).

The group \(U\) has odd order, so in \(U\rtimes\langle L\rangle\), Schur--Zassenhaus (or the elementary coprime-action conjugacy-of-complements theorem) gives one \(U\)-conjugacy orbit of involution lifts of \(L\). Its cardinality is \(|U|/|C_U(L)|=q^{u_n-f_{n,b}}\). The number of linear involutions with negative eigenspace dimension \(b\) is the number of ordered decompositions \(V=V_+\oplus V_-\), namely \({n\brack b}_q q^{b(n-b)}\). Multiplying proves the formula. Conjugacy in the full automorphism group preserves \(b\), giving exactly \(n+1\) classes.

For \(0<b<n\), substitution gives
\[
 b(n-b)+u_n-f_{n,b}=(n+1)2^{n-2}-b(n-b)+\mathbf1_{n\text{ odd},\,b\text{ even}}-\mathbf1_{n\text{ odd}}.
\]
Since \({n\brack b}_q=q^{b(n-b)}(1+O_n(q^{-1}))\), all mixed types have the same leading exponent \((n+1)2^{n-2}\) when \(n\) is even; when \(n\) is odd, even \(b\) have that exponent and odd \(b\) have one lower. The boundary classes have sizes \(I_{n,0}(q)=1\) and \(I_{n,n}(q)=q^{2^{n-1}-\mathbf1_{n\text{ odd}}}\), both lower order for every \(n\ge2\). Dividing by the total proves the limiting uniform distributions.

## Verification
The accompanying `verify.py` independently enumerates all odd-field automorphisms for the two-generator case by polynomial substitution, obtaining \(1+q^3+2q^2\) order-dividing-two automorphisms. In the three-generator case it exhausts the \(q^6\) non-linear automorphism coordinates over \(\mathbb F_3\) above a diagonal involution of each of the four sign types and checks the square by direct exterior multiplication, finding \((1,27,81,27)\) lifts. Algebraic checks compare closed-form group fixed-space counts and leading exponents for \(2\le n\le12\). These finite experiments support but cannot replace the general proof.

## Relationship to prior work
Bavula (2007/2010) proves the complete structural decomposition of automorphisms into inner, parity-preserving, and linear factors; that structural result and linearization by coprime action are expressly prior ingredients. Guimarães and Koshlukov (2020) study automorphisms of order two and \(\mathbb Z/2\mathbb Z\)-superalgebra structures of the *infinite-dimensional*, characteristic-zero Grassmann algebra. They do not supply the present finite-field cardinality or its odd/even dimension asymptotic distribution. The full-text passages of Bavula's automorphism-group theorem and the motivating paper's discussion of involutions and gradings were inspected. The 2025 survey concerns the infinite-dimensional case. Search results did not locate an equivalent all-rank finite-field count; this absence is not a proof of publication novelty.

## Limitations
The enumeration uses Bavula's established automorphism decomposition, rather than reproving its full nontrivial classification. The result holds for finite exterior algebras in odd characteristic only, and the asymptotic takes field order to infinity at fixed generator number. The formula counts labeled gradings, rather than distinguishing different graded polynomial-identity theories. Possible prior results in older or unindexed finite Grassmann grading literature remain an originality risk. No independent mathematical audit or publication-priority certification is claimed.

## References
1. V. V. Bavula, *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra*, arXiv:math/0703352 (first public March 12, 2007), Bulletin de la Société Mathématique de France 138 (2010), 39–117, especially Theorem 2.14 and Corollary 2.15. https://arxiv.org/abs/math/0703352
2. A. de Araújo Guimarães and P. Koshlukov, *Automorphisms and superalgebra structures on the Grassmann algebra*, arXiv:2009.00175 (first public September 1, 2020). https://arxiv.org/abs/2009.00175
3. A. Guimarães, *Interplay between Z2-gradings and automorphisms in the Grassmann algebra: a survey*, arXiv:2508.15628 (2025; later supporting context only). https://arxiv.org/abs/2508.15628
