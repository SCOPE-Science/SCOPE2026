# Support–gcd orbit classification for characteristic-two Rota–Baxter operators on evolution chains

## Finding

Let \(q=2^e\), with \(e\ge1\), and let \(n\ge2\). Consider the \(n\)-dimensional evolution algebra \(E_n\) over \(\mathbb F_q\) with natural basis \(e_1,\ldots,e_n\), zero mixed products, and
\[
e_i^2=e_{i+1}\quad(1\le i<n),\qquad e_n^2=0.
\]

The nonzero *linear weight-zero Rota–Baxter operators* are among the maps
\[
R_{\mathbf c}(e_i)=c_i e_n,\qquad
\mathbf c=(c_1,\ldots,c_n)\in\mathbb F_q^n.
\]
In fact, these are all the operators, including \(\mathbf c=0\). Their number \(q^n\) and their annihilator-valued nature are pre-existing structural facts, not the new enumerative claim.

The finding gives the complete **automorphism-conjugacy orbit classification**, including every orbit's size, its stabilizer, the full distribution by nonzero-coordinate support, and the total number of orbits. Set \(t=q-1\). The scalar \(c_n\) is invariant under conjugacy.

For a nonempty set \(J\subseteq\{1,\ldots,n-1\}\), define
\[
g(J)=\gcd\bigl(e,\{n-i:i\in J\}\bigr),\qquad
h(J)=2^{g(J)}-1.
\]
For any nonempty \(J\subseteq\{2,\ldots,n-1\}\), use the same definitions. The orbit structure is as follows:

1. **Vanishing terminal coefficient:** If \(c_n=0\), let \(J=\{1\le i<n:c_i\ne0\}\). For \(J=\varnothing\), there is one fixed operator. For each nonempty \(J\), exactly \(t^{|J|-1}h(J)\) distinct orbits have support exactly \(J\), and **every one** of them has orbit size \(t/h(J)\) and automorphism stabilizer order \(q h(J)\).
2. **Nonvanishing terminal coefficient:** Fix a specified \(c_n=s\in\mathbb F_q^\times\) and put \(J=\{2\le i<n:c_i\ne0\}\). The coordinate \(c_1\) is not an invariant. For \(J=\varnothing\), there is one orbit of size \(q\) and stabilizer order \(t\). For each nonempty \(J\), exactly \(t^{|J|-1}h(J)\) distinct orbits occur at the specified \(s,J\), every one having orbit size \(qt/h(J)\) and stabilizer order \(h(J)\).

Equivalently, for each divisor \(d\mid(q-1)\), let \(o_d\) be the multiplicative order of \(2\) modulo \(d\), with the convention \(o_1=1\), and let \(\varphi\) denote Euler's totient. Then the total orbit count has the compact arithmetic formula
\[
\boxed{\mathcal O_n(q)=
\frac{1}{q-1}\sum_{d\mid(q-1)}\varphi(d)
\left(q^{\lfloor(n-1)/o_d\rfloor}
+(q-1)q^{\lfloor(n-2)/o_d\rfloor}\right).}
\]

In particular,
\[
\boxed{\mathcal O_n(2)=3\cdot2^{n-2}\quad(n\ge2),\qquad \mathcal O_2(q)=q+1.}
\]

These formulas are exact for every \(e\ge1\) and \(n\ge2\), with no asymptotic or probabilistic assumption.

## Assumptions and scope

The algebra multiplication is \(\mathbb F_q\)-bilinear and commutative, but generally nonassociative. An algebra automorphism is an invertible \(\mathbb F_q\)-linear multiplication-preserving map. Two weight-zero Rota–Baxter operators are conjugate when \(R'=\phi R\phi^{-1}\) for some \(\phi\in\operatorname{Aut}(E_n)\). The weight-zero identity is
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)\bigr)\quad(x,y\in E_n).
\]
The stated stabilizers and orbit sizes are for this full algebra automorphism group, not for arbitrary linear changes of basis or unlabelled evolution-algebra isomorphisms.

## Proof

**1. Operator parametrization, recalled rather than claimed as new.** The natural-basis squares \(e_1^2,\ldots,e_{n-1}^2\) are independent, and \(\operatorname{Ann}(E_n)=\mathbb F_qe_n\). If a vector \(v\) has square zero, independence forces its first \(n-1\) coordinates to vanish, hence \(v\in\operatorname{Ann}(E_n)\). For any linear weight-zero operator \(R\), setting \(x=y\) in the Rota–Baxter identity gives \(R(x)^2=R(2xR(x))=0\), so every image lies in the annihilator. Conversely, every linear annihilator-valued map satisfies the identity because all products on both sides vanish. Thus \(R_{\mathbf c}\) runs through the entire known operator set bijectively.

**2. The complete automorphism group.** For \(a\in\mathbb F_q^\times\), \(b\in\mathbb F_q\), define
\[
\phi_{a,b}(e_1)=a e_1+b e_n,
\qquad \phi_{a,b}(e_i)=a^{2^{i-1}}e_i\quad(2\le i\le n).
\]
Each is a multiplication-preserving invertible map. Conversely, let \(\phi\) be an automorphism and write \(\phi(e_1)=\sum_{j=1}^n a_j e_j\). Repeatedly applying \(\phi(e_{i+1})=\phi(e_i)^2\) shows that \(\phi(e_i)\) is determined by \(\phi(e_1)\); invertibility forces \(a_1\ne0\). For \(2\le j<n\), use \(\phi(e_1)\phi(e_j)=0\). The coefficient of \(e_{j+1}\) is \(a_j a_1^{2^{j-1}}\), because \(\phi(e_j)\) has coefficient \(a_1^{2^{j-1}}\) at \(e_j\) and no earlier nonzero coordinate. Thus \(a_j=0\) for every \(2\le j<n\). The remaining coefficient \(a_n=b\) is free, giving exactly the displayed family. The group therefore has order \(q(q-1)\). This also reconstructs the relevant chain specialization of the established automorphism calculations in the cited literature, rather than treating that automorphism description as new.

**3. Conjugation action.** Put \(L=2^{n-1}\). Compare \(R'\phi_{a,b}=\phi_{a,b}R\) on the basis. Because \(\phi_{a,b}(e_n)=a^Le_n\), one obtains
\[
\boxed{\begin{aligned}
c_n'&=c_n,\\
c_i'&=a^{L-2^{i-1}}c_i\quad(2\le i<n),\\
c_1'&=a^{L-1}c_1-\frac ba c_n.
\end{aligned}}
\]
In characteristic two the minus sign equals plus, but retaining the formula clarifies the affine action. These formulas are necessary and sufficient for conjugacy because every automorphism has already been listed.

**4. Stabilizers from supports.** For a coefficient \(c_n=0\), the parameter \(b\) acts trivially, and \(a\) fixes \(\mathbf c\) precisely if \(a^{L-2^{i-1}}=1\) for every \(i\) in the nonzero support \(J\subseteq\{1,\ldots,n-1\}\). Since the multiplicative group has odd order \(t=2^e-1\) and
\[
L-2^{i-1}=2^{i-1}(2^{n-i}-1),
\]
the number of admissible choices of \(a\) is
\[
\gcd\bigl(2^e-1,\{2^{n-i}-1:i\in J\}\bigr)
=2^{\gcd(e,\{n-i:i\in J\})}-1=h(J).
\]
Here the last equality follows by the elementary Euclidean-algorithm identity \(\gcd(2^r-1,2^s-1)=2^{\gcd(r,s)}-1\), iterated over \(J\). Including the \(q\) arbitrary choices of \(b\), the stabilizer order is \(q h(J)\); orbit–stabilizer gives \(t/h(J)\). For empty support the zero operator is fixed.

For \(c_n=s\ne0\), every admissible \(a\) uniquely determines \(b\) to preserve \(c_1\), so there is **no free \(b\)-stabilizer**. The other invariant support is \(J\subseteq\{2,\ldots,n-1\}\), again with \(h(J)\) admissible scalars. For nonempty \(J\) the orbit size is \(qt/h(J)\). For \(J=\varnothing\) every \(a\) has its unique compatible \(b\), yielding stabilizer \(t\) and orbit size \(q\).

**5. Exact support counts.** When \(c_n=0\) and a nonempty support \(J\) is fixed, there are \(t^{|J|}\) coefficient vectors. Dividing by their common orbit size \(t/h(J)\) gives \(t^{|J|-1}h(J)\) orbits. For fixed nonzero \(c_n=s\), each nonempty support \(J\subseteq\{2,\ldots,n-1\}\) allows \(q\) unrestricted values of \(c_1\) and \(t^{|J|}\) other coefficient assignments. Dividing \(qt^{|J|}\) by \(qt/h(J)\) gives the same expression. When \(J\) is empty there is one orbit for each specified \(s\). This proves the complete support-and-size classification.

**6. Divisor-sum compression.** The cyclic group \(\mathbb F_q^\times\) has \(\varphi(d)\) elements of order \(d\) for each \(d\mid t\). If such an element acts on the \(c_n=0\) coefficient space, it fixes \(c_i\) freely precisely when \(d\mid 2^{n-i}-1\); equivalently \(o_d\mid n-i\). Thus its fixed vectors number \(q^{\lfloor(n-1)/o_d\rfloor}\). Burnside's lemma gives the first term of the boxed formula. For a fixed \(c_n=s\ne0\), the affine \(b\) coordinate kills the \(c_1\) degree of freedom, and the residual cyclic action on \(c_2,\ldots,c_{n-1}\) has \(q^{\lfloor(n-2)/o_d\rfloor}\) fixed vectors. Multiplying that orbit count by the \(q-1\) possible nonzero \(s\)'s gives the second term.

When \(q=2\), the only divisor is \(d=1\), giving \(\mathcal O_n(2)=2^{n-1}+2^{n-2}\). When \(n=2\), the \(c_2=0\) sector has the zero operator and one orbit of nonzero \(c_1\) (two orbits), while each of the \(q-1\) nonzero values of \(c_2\) supplies one orbit, totaling \(q+1\).

## Verification

`verify.py` is a self-contained Python 3 implementation using exact arithmetic in \(\mathbb F_2,\mathbb F_4,\mathbb F_8\). It checks the **complete** algebra automorphism set by exhaustive linear-matrix enumeration in the cases \((q,n)=(2,3),(4,2)\). For every coefficient vector in ten small \((q,n)\) cases, it directly enumerates the \(q(q-1)\) conjugation images, compares actual orbit size with the support–gcd prediction, partitions the full \(q^n\) coefficient space, and independently evaluates both the support-subset and divisor-sum formulas. Representative outputs include \(\mathcal O_3(4)=14\), \(\mathcal O_4(4)=48\), \(\mathcal O_3(8)=24\), and \(\mathcal O_4(8)=150\). The script prints `VERIFY_OK` when every comparison succeeds. These finite computations corroborate but do not replace the proof for all \(e,n\).

## Relationship to prior work

The 2019 paper by Mukhamedov–Khakimov–Omirov–Qaralleh (*Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex*, arXiv:1805.10285, Theorem 5.1) already describes automorphisms of these algebras, under a characteristic-zero hypothesis. The chain automorphism family above is reconstructed directly and is **not** claimed as a new independent automorphism theorem.

Qaralleh–Mukhamedov–Khakimov's *Local Rota–Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex*, arXiv:2606.22623v1 (first public June 21, 2026), and their preceding arXiv:2601.08669v1 study ordinary and local operators in **characteristic zero**. The ordinary annihilator-valued characterization in characteristic two is also known and is a prerequisite, not the proposed contribution. Earlier odd-characteristic chain computations concern conjugacy of a larger ordinary-operator family. They do not enumerate the even-characteristic orbit supports and stabilizers or give the present \(\gcd\)- and multiplicative-order formulas.

The new claim concerns precisely the **complete automorphism-conjugacy orbit-size and support distribution** for every binary extension field and chain length, including the compact divisor-sum count. It does not claim novelty for the existence of the operators, for the elementary group structure, or for Burnside's lemma itself.

## Limitations

The theorem is for the **pure chain** \(e_i^2=e_{i+1}\), not arbitrary maximal-nilindex evolution algebras with additional long-range square coefficients; those may have smaller automorphism groups. The field must be finite of characteristic two. Weight-one operators, nonlinear witness maps, isomorphism classes of distinct evolution algebras, and arbitrary linear-conjugacy orbits are not addressed. The computations only exhaust the specified small instances. Literature priority is qualified by the accessibility of older or unindexed works and by the fact that several structural ingredients are previously known; an independent mathematical audit is not claimed.

## References

1. I. Qaralleh, F. Mukhamedov, O. Khakimov, “Local Rota–Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex,” arXiv:2606.22623v1 (first public 2026-06-21), https://arxiv.org/abs/2606.22623.
2. I. Qaralleh, F. Mukhamedov, O. Khakimov, “Rota–Baxter operators of nilpotent evolution algebras with maximal nilindex,” arXiv:2601.08669v1 (2026-01-13), https://arxiv.org/abs/2601.08669.
3. F. Mukhamedov, O. Khakimov, B. Omirov, I. Qaralleh, “Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex,” arXiv:1805.10285v2 (2018), https://arxiv.org/abs/1805.10285; Journal of Algebra and its Applications 18 (2019), article 1950233.
