# Order-of-two resonances and affine idempotent quandles in modular dihedral quandle algebras

## Finding

Let \(p\) be an odd prime, \(k\) any field of characteristic \(p\), and \(R_p=\mathbb Z/p\mathbb Z\) the dihedral quandle with operation \(i\triangleright j=2j-i\). Write \(Q_p(k)=k[R_p]\) for its nonassociative quandle algebra, with basis \(e_i\) and multiplication \(e_i\star e_j=e_{2j-i}\). Set
\[
 o_p=\operatorname{ord}_p(2),\qquad L_p=\operatorname{lcm}(2,o_p),\qquad d_p=1+\left\lfloor\frac{p-2}{L_p}\right\rfloor.
\]
The affine scheme of idempotents \(f\star f=f\) of \(Q_p(k)\) is the **disjoint union of one reduced point and a reduced affine space of dimension \(d_p\)**. There is an explicit polynomial parametrization of the latter over \(\mathbb F_p\). In particular, for any finite field \(\mathbb F_q\) with characteristic \(p\),
\[
 \#\operatorname{Idem}(Q_p(\mathbb F_q))=1+q^{d_p}.
\]
Furthermore, the set of nonzero idempotents is closed under \(\star\), and under its affine coordinates its operation is exactly \((x,y)\mapsto -x+2y\) on the additive vector group \(k^{d_p}\). Thus it is the Takasaki/core quandle of this vector group, not merely a set of the same size. The first odd prime with \(d_p>1\) is \(p=17\), where \(d_{17}=2\); therefore \(Q_{17}(\mathbb F_{17})\) has \(290\) idempotents, including \(272\) non-basis, nonzero ones.

## Assumptions and scope

All statements hold for **every odd prime** \(p\), every characteristic-\(p\) field \(k\), and after arbitrary extension of \(k\); the scheme claim uses its functor of points for commutative \(k\)-algebras. The quandle algebra is the linear extension of the right-translation operation \(i\triangleright j=2j-i\), and its multiplication is not generally associative or commutative. The integer \(o_p\) is the least positive \(r\) with \(2^r\equiv1\pmod p\). The result does not describe characteristic unequal to the quandle modulus or composite quandle moduli.

## Proof

**1. Group-ring realization.** Let \(A=k[t]/(t^p-1)\), an associative commutative algebra. The linear identification \(e_i\leftrightarrow t^i\) converts the quandle product into
\[
 f\star g=T_{-1}(f)T_2(g),\qquad T_a(t)=t^a\quad(a\in\mathbb F_p^\times),
\]
where the product on the right is the usual multiplication in \(A\). Since the characteristic is \(p\), put \(u=t-1\) and identify \(A=k[u]/(u^p)\). Let \(J=uA\) and \(\varepsilon(f)=f(1)\). The augmentation obeys \(\varepsilon(f\star g)=\varepsilon(f)\varepsilon(g)\).

**2. The zero-augmentation branch.** If \(f\star f=f\), then \(a=\varepsilon(f)\) satisfies \(a^2=a\). Over a field \(a=0\) or \(1\). On the branch \(a=0\), \(f\in J\) and \(f=T_{-1}(f)T_2(f)\in J^2\). Inductively \(f\in J^{2^r}\) for every \(r\), hence \(f=0\). This is also an identity of solutions over an arbitrary commutative base ring once the augmentation idempotent is restricted to \(a=0\), so the branch is scheme-theoretically a single reduced point.

**3. Linearization of the other branch.** On the branch \(\varepsilon(f)=1\) write \(f=1+v\), \(v\in J\). Because \(J^p=0\) and \(1,2,\ldots,p-1\) are units, the truncated series
\[
 \exp(h)=\sum_{n=0}^{p-1}\frac{h^n}{n!},\qquad
 \log(1+v)=\sum_{n=1}^{p-1}\frac{(-1)^{n+1}v^n}{n}
\]
are inverse polynomial group isomorphisms from \((J,+)\) to \((1+J,\cdot)\), over every commutative \(k\)-algebra. The operators \(T_a\) commute with these series. Consequently \(f=\exp(h)\) is idempotent precisely when
\[
 (I-T_{-1}-T_2)h=0.\tag{1}
\]
Thus the augmentation-one idempotent scheme is the vector space \(K=\ker(I-T_{-1}-T_2)\) transported by an explicit polynomial isomorphism.

**4. Resonant eigenspaces.** The multiplicative group \(\mathbb F_p^\times\) acts on \(J\) via \(a\mapsto T_a\), with order \(p-1\), invertible in \(k\). The filtration \(J\supset J^2\supset\cdots\supset J^{p-1}\supset0\) has one-dimensional successive quotients \(J^j/J^{j+1}\), on which \(T_a\) acts by \(a^j\). Maschke splitting implies that \(J\) is the direct sum of one copy of each character \(a\mapsto a^j\), for \(1\le j\le p-1\). Explicit character projectors are
\[
 E_j=\frac{1}{p-1}\sum_{a\in\mathbb F_p^\times}a^{-j}T_a,
 \quad w_j=E_j(u^j).
\]
The leading coefficient of \(w_j\) is \(u^j\); thus \(w_j\ne0\), and \(T_a(w_j)=a^jw_j\). Equation (1) holds on the \(j\)-th line if and only if
\[
 1=(-1)^j+2^j\quad\text{in }\mathbb F_p.
\]
For even \(j\) this would force \(2^j=0\), impossible. For odd \(j\), it is exactly \(2^{j-1}=1\), so the admissible exponents are
\[
 j\in\{1,1+L_p,1+2L_p,\ldots\}\cap[1,p-1].
\]
There are exactly \(d_p=1+\lfloor(p-2)/L_p\rfloor\) such exponents. Therefore the nonzero idempotents have the explicit parametrization
\[
 (\lambda_j)_{j\text{ admissible}}\longmapsto
 \exp\Bigl(\sum_j\lambda_jw_j\Bigr),
\]
an affine-space isomorphism with polynomial inverse \(f\mapsto (E_j\log f)_j\). Both branches are reduced; together they exhaust the full idempotent scheme, including its infinitesimal structure.

**5. Quandle structure.** On \(K\) the two operators act as \(T_{-1}=-I\) and \(T_2=2I\). For \(x,y\in K\),
\[
 \exp(x)\star\exp(y)
 =\exp(T_{-1}x+T_2y)=\exp(-x+2y).
\]
The product therefore stays in the augmentation-one idempotent locus and is the Takasaki operation. The extra zero idempotent is not in this subquandle.

**6. First resonance.** For the odd primes \(3,5,7,11,13\), one checks \(o_p=2,4,3,10,12\), respectively, giving \(d_p=1\). At \(p=17\), \(o_{17}=8\) and the admissible weights are \(1,9\), so \(d_{17}=2\). Over \(\mathbb F_{17}\), the affine component has \(17^2=289\) points; exactly \(17\) are the original basis idempotents, leaving \(272\) new non-basis nonzero idempotents.

## Verification

The accompanying standalone `verify.py` uses modular polynomial arithmetic, derives the kernel of (1) by finite-field Gaussian elimination, and verifies the predicted dimensions for primes \(3,5,7,11,13,17,19,31,127\). It checks the weight eigenvalue equations and direct original-basis idempotence on kernel generators through \(p=31\), including a two-parameter combination and the affine quandle law at resonance primes. Direct exhaustive enumeration of all elements of \(\mathbb F_p[R_p]\) at \(p=3,5\) confirms \(4\) and \(6\) idempotents. The program reports `VERIFY_OK`. These finite checks corroborate, but do not prove, the universal theorem.

## Relationship to prior work

Quandle linearization and the standard dihedral operation occur in the earlier quandle and quandle-ring literature [1,2]. Idempotents of integral quandle rings and small dihedral cases were studied in [3]. A published mathematical record [4] already identifies the affine idempotent line for \(R_3\) in characteristic \(3\); that case is a strict specialization of this theorem and is **not claimed as new**. The present claim concerns the all-odd-prime modular spectrum \(d_p\), the first higher-dimensional jump at \(p=17\), the reduced scheme structure, and the internal Takasaki quandle operation. Later studies [5,6] concern related idempotent phenomena in dihedral and other quandle algebras, often over integral coefficient rings; their accessible statements did not establish this modular all-prime classification. A closely related 2026 Fourier-analysis preprint [7] could not be inspected in full and presents a residual risk of stronger or equivalent prior coverage.

## Limitations

The theorem is restricted to coefficient characteristic equal to an **odd prime modulus**. Nothing is asserted for even/composite moduli or other coefficient characteristics. The 2026 Fourier preprint [7] was not read in full; no assertion is made about what its unseen sections contain. Independent scholarly assessment and a comprehensive survey of all specialized literature have not been performed. Finite-field verification is not a replacement for the characteristic-free-in-\(k\) proof above.

## References

[1] J. S. Carter, A. S. Crans, M. Elhamdadi, M. Saito, *Cohomology of Categorical Self-Distributivity*, arXiv:math/0607417 (first public version 2006-07-18), https://arxiv.org/abs/math/0607417 .

[2] M. Elhamdadi, B. Fernando, B. Tsvelikhovskiy, *Ring Theoretic Aspects of Quandles*, arXiv:1805.05908, https://arxiv.org/abs/1805.05908 .

[3] V. Bardakov, I. B. S. Passi, M. Singh, *Zero-divisors and Idempotents in Quandle Rings*, arXiv:2001.06843, https://arxiv.org/abs/2001.06843 .

[4] Published published-finding corpus finding, *A characteristic-three idempotent line in the quandle algebra of \(R_3\)*, published published-finding corpus record identifier 06aa9c19e539 .

[5] M. Sangare and A. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550, https://arxiv.org/abs/2608.01550 .

[6] *A Further Study of Quandles and Quandle Rings*, arXiv:2608.09149, https://arxiv.org/abs/2608.09149 .

[7] M. Elhamdadi, A. Ta, and collaborators, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799, https://arxiv.org/abs/2609.03799 (abstract and metadata consulted; full text not inspected).
