# A universal sign bias for classified finite-field permutation binomials

## Finding

Let \(q\ge3\) be an odd prime power and \(e\ge2\). Define
\[
Q=q^e,\qquad L=\frac{Q-1}{q-1},\qquad
F_{r,a}(X)=X^r(X^{q-1}+a)\in\mathbb F_Q[X].
\]
Fix a positive integer \(r\) satisfying \(\gcd(r,q-1)=1\) and, for some \(1\le h<e\) with \(\gcd(h,e)=1\),
\[
r\frac{q^h-1}{q-1}\equiv1\pmod L.
\]
Let \(\chi_q:\mathbb F_q^\times\to\{\pm1\}\) be the quadratic character, and let \(\operatorname{N}\) denote the relative norm from \(\mathbb F_Q\) to \(\mathbb F_q\). For any \(a\in\mathbb F_Q^\times\) with \(\operatorname{N}(-a)\ne1\), the induced permutation has sign
\[
\boxed{\operatorname{sgn}(F_{r,a})
=\delta_{Q,r}\chi_q\bigl(\operatorname{N}(a)-(-1)^e\bigr),\qquad
\delta_{Q,r}=\begin{cases}
(-1)^{(r-1)/2},&Q\equiv1\pmod4,\\
1,&Q\equiv3\pmod4.
\end{cases}}
\]
Sign \(+1\) means an even permutation and sign \(-1\) an odd permutation. Put \(\varepsilon_{q,e}=\chi_q((-1)^{e+1})\). Then the exact numbers of eligible coefficients giving even and odd permutations are
\[
\boxed{N_{\mathrm{even}}=\frac L2(q-2-\delta_{Q,r}\varepsilon_{q,e}),\qquad
N_{\mathrm{odd}}=\frac L2(q-2+\delta_{Q,r}\varepsilon_{q,e}).}
\]
In particular, \(N_{\mathrm{even}}-N_{\mathrm{odd}}=-\delta_{Q,r}\varepsilon_{q,e}L\). **No admissible fixed-exponent coefficient family has equal populations of even and odd permutations.** For example, at \((q,e,r)=(3,2,1)\), all four permitted coefficients induce even permutations; at \((5,2,1)\) the counts are six even and twelve odd, while \((5,2,7)\) reverses them.

## Assumptions and scope

The field characteristic is odd; \(e\ge2\); \(r\) is a positive admissible exponent satisfying the displayed arithmetic conditions. The relative norm is \(\operatorname{N}(a)=a^L\), and the coefficient range is exactly \(a\in\mathbb F_Q^\times\) with \(\operatorname{N}(-a)\ne1\). These conditions are sufficient for permutation because of the explicit factorization in the proof; the recent cited classification also makes them necessary for this binomial family. The counts are for each fixed \(r\); no assertion is made about the number of distinct functions after varying \(r\).

## Proof

**1. Factorization and its domain.** The standard identity \(\gcd(\ell_h(q),\ell_e(q))=\ell_{\gcd(h,e)}(q)=1\), where \(\ell_j(q)=(q^j-1)/(q-1)\), implies \(\gcd(r,L)=1\). Together with \(\gcd(r,q-1)=1\), this gives \(\gcd(r,Q-1)=1\). Hence \(M_r:x\mapsto x^r\) is a permutation of \(\mathbb F_Q\). Since
\[
r(q^h-1)\equiv q-1\pmod{Q-1},
\]
the polynomial functions on \(\mathbb F_Q\) satisfy
\[
F_{r,a}=T_{h,a}\circ M_r,\qquad T_{h,a}(x)=x^{q^h}+ax.
\]
This holds at zero as well as on nonzero elements.

**2. Determinant of the linearized map.** The map \(T_{h,a}\) is \(\mathbb F_q\)-linear. Extend scalars to an algebraic closure of \(\mathbb F_q\). The \(e\) embeddings of \(\mathbb F_Q\) diagonalize multiplication by \(a\) with diagonal entries \(a,a^q,\ldots,a^{q^{e-1}}\), while \(x\mapsto x^{q^h}\) permutes the embedding coordinates in one \(e\)-cycle, as \(\gcd(h,e)=1\). The determinant expansion of a diagonal matrix plus a cyclic permutation matrix has exactly two nonzero terms: the product of diagonal entries and the signed cycle. Consequently
\[
\det_{\mathbb F_q}(T_{h,a})=
\operatorname{N}(a)+(-1)^{e-1}
=\operatorname{N}(a)-(-1)^e.
\]
Thus the coefficient condition is precisely invertibility of \(T_{h,a}\), and the displayed composition is a permutation.

**3. Parity of a linear map.** Every invertible \(\mathbb F_q\)-linear transformation of \(\mathbb F_q^e\), viewed as a permutation of its \(q^e\) points, has sign \(\chi_q\) of its determinant. Indeed, elementary transvections have odd-prime order and therefore even sign. Diagonal changes of basis reduce to multiplication by \(\lambda\in\mathbb F_q^\times\) in one coordinate: on each of the odd number \(q^{e-1}\) of coordinate fibers, its permutation sign is \(\chi_q(\lambda)\). These generators establish the assertion. Hence
\[
\operatorname{sgn}(T_{h,a})=\chi_q(\operatorname{N}(a)-(-1)^e).
\]

**4. Power-map parity.** On the \(Q-1\) nonzero elements, a choice of generator identifies \(M_r\) with multiplication by \(r\) on \(\mathbb Z/(Q-1)\). Write \(Q-1=2^t m\), with \(m\) odd. The Chinese remainder theorem shows the sign equals the sign on \(\mathbb Z/2^t\mathbb Z\), since the odd-factor sign is raised to the even power \(2^t\). For \(t=1\) this sign is one. For \(t\ge2\), decompose the residues modulo \(2^t\) by their exact power of two. The stratum corresponding to units modulo \(2^j\) is permuted by multiplication by \(r\). For \(j\ge3\), \(|(\mathbb Z/2^j\mathbb Z)^\times|=2^{j-1}\), but every unit has order dividing \(2^{j-2}\); hence the permutation is an even number of equal-length cycles and has positive sign. The \(j=1\) stratum is fixed, and the \(j=2\) stratum is transposed exactly when \(r\equiv3\pmod4\). Therefore
\[
\operatorname{sgn}(M_r)=\begin{cases}
(-1)^{(r-1)/2},&4\mid Q-1,\\
1,&Q-1\equiv2\pmod4,
\end{cases}
\]
with zero fixed and no effect on sign. Multiplying the signs in Steps 3 and 4 proves the asserted sign formula.

**5. Exact coefficient counts.** The norm \(\mathbb F_Q^\times\to\mathbb F_q^\times\) is surjective with every fiber of size \(L\). Put \(b_0=(-1)^e\) and \(b=\operatorname{N}(a)\); the admissible values are \(b\in\mathbb F_q^\times\setminus\{b_0\}\), each attained by \(L\) coefficients. By translation and the vanishing of the nontrivial quadratic-character sum,
\[
\sum_{\substack{b\in\mathbb F_q^\times\\b\ne b_0}}
\chi_q(b-b_0)
=-\chi_q(-b_0)=-\varepsilon_{q,e}.
\]
There are \((q-2)L\) eligible coefficients and their signed total is \(-\delta_{Q,r}\varepsilon_{q,e}L\). Since signed total is the even count minus the odd count, solving the two linear equations gives the boxed formulas. Because \(L>0\), their difference is never zero.

## Verification

The standalone Python 3 script `VERIFY.py` uses no external dependencies. It constructs small extension fields by finding an irreducible polynomial, evaluates the binomial directly on every field element, determines the sign from its cycle decomposition, independently calculates norms and quadratic characters, and compares exact even/odd coefficient counts. Fourteen admissible parameter cases across characteristics three, five, seven and the nonprime base field \(q=9\) pass; 609 individually evaluated permutations agree with the proof. The output of the included script is recorded in `VERIFY_OUT.txt`. These finite cases test boundaries but do not replace the universal algebraic argument.

## Relationship to prior work

Fan (arXiv:2609.20354, first public 17 September 2026) and Ni–Pang–Yu–Yuan (arXiv:2609.28595, first public 23 September 2026) independently establish the permutation criterion for the same binomial family. Their accessible abstracts explain the Frobenius-linearized composition but do not state the permutation sign distribution. A published contemporary result, *Collision rigidity and exact enumeration for coprime-index permutation binomials*, classifies equal permutation functions across index classes and counts those functions. Its full `RESULT.md` was examined and gives no even/odd permutation-sign count. These enumeration theorems are not themselves counts by permutation parity: the sign formula and coefficient imbalance require the determinant and power-map calculations above. The familiar determinant-character identity for general linear maps is used as a lemma, not claimed as a discovery.

## Limitations

The claim concerns odd characteristic and fixed admissible exponent \(r\). It does not enumerate the parity of all distinct functions when exponents or index classes vary, nor does it claim group generation or cycle-type classification. The arXiv abstracts were verified, but full text of both closely relevant September 2026 classification papers was not available through the attempted lawful sources; a hidden parity subsection in either paper remains a material originality risk. Searches and accessible-text inspection cannot prove universal novelty. Finite verification alone cannot establish infinite results.

## References

1. Xiang Fan, *A complete classification of permutation binomials of the form \(X^r(X^{q-1}+a)\) over finite fields*, arXiv:2609.20354v1 (17 September 2026). https://arxiv.org/abs/2609.20354
2. Junna Ni, Xuan Pang, Jianhua Yu and Pingzhi Yuan, *Permutation binomials of the form \(X^r(X^{q-1}+a)\) over finite fields*, arXiv:2609.28595v1 (23 September 2026). https://arxiv.org/abs/2609.28595
3. *Collision rigidity and exact enumeration for coprime-index permutation binomials*, published research result, 18 September 2026. https://github.com/published-finding corpus/2026/blob/main/2026/9/18/SCOPE-coprime-index-permutation-binomial-collisions--249fad2fb294/RESULT.md
