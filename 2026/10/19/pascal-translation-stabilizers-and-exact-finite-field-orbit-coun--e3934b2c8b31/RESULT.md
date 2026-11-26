# Exact characteristic-free stabilizer rigidity and finite orbits for the canonical Bézout Rota–Baxter operator

## Finding

Let \(K\) be any field and \(n\ge2\). On the matrix units of \(M_n(K)\) define the canonical weight-zero operator
\[
B_0(E_{ij})=\begin{cases}
\sum_{r\ge0}E_{i+r,j+r+1},&i\le j,\\
-\sum_{r\ge1}E_{i-r,j-r+1},&i>j,
\end{cases}
\]
omitting out-of-range units. For \(t\in K\), let \(P_t\) be substitution \(f(x)\mapsto f(x+t)\) on polynomials of degree less than \(n\), in the increasing monomial basis. Its \((i,j)\) entry is \(\binom{j-1}{i-1}t^{j-i}\) for \(i\le j\) and zero otherwise. The Bézout translation symmetry is known; the assertion here is that there are **no additional finite-dimensional inner symmetries in any characteristic**, including when \(n\) exceeds the characteristic. Writing \(\operatorname{Ad}_U(X)=UXU^{-1}\), the entire stabilizer for conjugation on operators is
\[
\operatorname{Stab}_{\operatorname{PGL}_n(K)}(B_0)=\{\operatorname{Ad}_{P_t}:t\in K\}\cong(K,+).
\]
Nonzero scalar multiples of \(B_0\) lie in its inner orbit; the inner orbit of \(B_0^\top(X)=(B_0(X^{\mathsf T}))^{\mathsf T}\) is disjoint. Over \(K=\mathbb F_q\) each has cardinality \(\lvert\operatorname{GL}_n(q)\rvert/[q(q-1)]\), so their union has twice this cardinality, with \(\lvert\operatorname{GL}_n(q)\rvert=\prod_{j=0}^{n-1}(q^n-q^j)\). This is a count of the two explicit canonical orbits, not a classification of extremal operators in positive characteristic.

## Proof

**Inverse description and the weight-zero identity.** Put \(W=\operatorname{span}(e_1,\ldots,e_{n-1})\), \(\mathcal B=\{b:\operatorname{im}b\subseteq W\}\), \(\mathcal K=\{b:bW=0\}\), and \(S=\sum_{i=1}^{n-1} E_{i+1,i}\). The unit formula vanishes on \(\mathcal K\) and lands in \(\mathcal B\). For a unit \(E_{ij}\) with \(i<n\), \(E_{ij}S-SE_{ij}=E_{i,j-1}-E_{i+1,j}\) with the first term absent if \(j=1\); applying \(B_0\) telescopes to \(E_{ij}\). Thus \(\operatorname{im}B_0=\mathcal B\) and by rank-nullity \(\ker B_0=\mathcal K\). The inverse of the induced map from \(M_n(K)/\mathcal K\) to \(\mathcal B\) is \(\delta(b)=bS-Sb+\mathcal K\). Since \(\mathcal B\mathcal K\subseteq\mathcal K\) and \(\mathcal K\mathcal B=0\), \(\delta\) is a derivation into the quotient bimodule. For \(b=B_0(x),c=B_0(y)\) it gives \(by+xc+\mathcal K=b\delta(c)+\delta(b)c=\delta(bc)\). Applying \(B_0\) proves the weight-zero identity \(B_0(x)B_0(y)=B_0(B_0(x)y+xB_0(y))\).

**Upper bound on inner symmetries.** If \(\operatorname{Ad}_U\) stabilizes \(B_0\), it preserves \(\mathcal B\), so \(UW=W\), and it preserves \(\mathcal K\). Commutation with the induced map is equivalent to commutation with its inverse \(\delta\). Thus for such \(U\) stabilization is equivalent to \([b,D]\in\mathcal K\) for all \(b\in\mathcal B\), where \(D=USU^{-1}-S\). Take for \(b\) a projection onto \(W\). The commutator condition shows that \(DW\subseteq W\). Taking all endomorphisms of \(W\) extended by zero shows that \(D|_W\) commutes with their full matrix algebra, so \(D|_W=tI|_W\) for some \(t\in K\). Conversely this restriction implies \([b,D]W=0\) for every \(b\in\mathcal B\). In particular, on \(Ue_j\in W\) for \(1\le j<n\) we have \(Ue_{j+1}=(S+tI)Ue_j\).

Write \(w=Ue_1\). The last coordinate of \((S+tI)^j w\) is zero for \(0\le j\le n-2\). For each \(j\) this last coordinate is \(w_{n-j}\) plus a combination of \(w_{n-j+1},\ldots,w_n\); using the equations successively gives \(w_2=\cdots=w_n=0\). Hence \(w=ce_1\) for \(c\ne0\) and the column recurrence gives \(U=cP_t\). Conversely \(P_t W=W\) and its columns obey that recurrence, so \((P_tSP_t^{-1}-S)|_W=tI|_W\) and \(P_t\) stabilizes \(B_0\). Substitution gives \(P_tP_u=P_{t+u}\); the diagonal ones and the \((1,2)\) entry distinguish projective classes. No factorials or binomial coefficients are divided out in the upper bound.

**Orbits.** Each nonzero summand of \(B_0(E_{ij})\) raises the degree \(j-i\) by one. Conjugating the operator by \(\operatorname{Ad}_{\operatorname{diag}(1,c,\ldots,c^{n-1})}\) therefore scales it by \(c^{-1}\). The common kernel of the image algebra \(\mathcal B\) is zero, while that of the transpose image \(\{b:be_n=0\}\) is the line \(Ke_n\). Common-kernel dimension is invariant under inner conjugation, so the two orbits are disjoint. Transposition intertwines the actions via \(U\mapsto U^{-\mathsf T}\). Each stabilizer in \(\operatorname{GL}_n(q)\) consequently has order \(q(q-1)\), giving the counts.

**Extremal nilpotency as context.** The degree shift gives \(B_0^{2n-1}=0\). Iterating on \(E_{n1}\) for \(n-1\) steps gives \((-1)^{n-1}E_{11}\), and the next \(n-1\) steps give \((-1)^{n-1}E_{1n}\): to achieve the only available last degree one must use the row-one, zero-shift summand at each step from \(E_{11}\). Thus the index is \(2n-1\) in all characteristics.

## Relationship to prior work

Ogievetsky and Popov, *R-matrices in rime*, [arXiv:0704.1947v3](https://arxiv.org/abs/0704.1947), §5, equation (121), use the divided difference \(D_0 f(x,y)=(f(x,y)-f(y,x))/(x-y)\) on the subspace of degree less than \(n\) in each variable. They explicitly describe translation invariance in the paragraph after (126); their §5.4 gives the partial-trace map (160) and corresponding Rota–Baxter formula (169). In the increasing basis \(e_i=x^{i-1}\), the contraction on a matrix unit acts at \(e_k\) by \((I\otimes e_j^*)D_0(e_k\otimes e_i)\), where \(e_j^*\) is the coefficient of \(x^{j-1}\) on the second copy. For \(k>i\) this gives \(e_{k-j+i-1}\) when \(i\le j\le k-1\); for \(k<i\) it gives \(-e_{k-j+i-1}\) when \(k\le j\le i-1\); otherwise it is zero. This is exactly the displayed \(B_0\). Simultaneously translating the two variables leaves the denominator \(x-y\) and the swap equivariant, immediately explaining the prior translation subgroup on this same operator. The finite-dimensional upper bound above does not assume that an arbitrary linear symmetry of the truncated space is a substitution, or that an infinitesimal generator determines it in positive characteristic.

Gubarev, *Extremal Rota–Baxter operators on matrix algebras*, [arXiv:2609.05647v1](https://arxiv.org/abs/2609.05647), equation (2), Theorem 1.1 and §4, gives the same canonical form and, in characteristic zero, the extremal weight-zero classification up to inner automorphism, transpose and nonzero scalar. No priority is asserted here for that classification, the Bézout realization, or the observation of translation invariance. The result isolates the exact stabilizer rigidity over arbitrary fields and its counted disjoint finite-field orbits.

## Verification scope

The companion `verify.py` contains finite checks of the identity, translation and scalar conjugations, and top nilpotent power over prime fields of orders two, three and five in dimensions two through five. Its exhaustive stabilizer tests are confined to \(\operatorname{GL}_2(2),\operatorname{GL}_3(2),\operatorname{GL}_2(3),\operatorname{GL}_3(3)\). The proof of the upper bound and orbit formulas is algebraic and is not an extrapolation from these cases.
