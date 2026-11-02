# Diagonal compatible relations and the sharp density exponent for two-level Clifford monoids

## Finding
Let \(G\) be an arbitrary **finite** group, with identity \(e\), and let \(E_2=\{0<1\}\) denote the two-element meet semilattice. Set \(S=E_2\times G\) with multiplication \((i,g)(j,h)=(\min(i,j),gh)\). A diagonal subsemigroup is a reflexive binary relation on \(S\) compatible with multiplication. Write \(\mathcal N(G)\) for the poset of normal subgroups, and, for \(N\le M\) in this poset, define
\[
I(N,M)=|\{H\triangleleft G:N\le H\le M\}|.
\]

**Classification.** Every diagonal subsemigroup \(\rho\) is specified uniquely by a pair of normal subgroups \(N\le M\) and two independent choices \(X,Y\in\{\varnothing\}\cup\{H\triangleleft G:N\le H\le M\}\). Here \(\varnothing\) is a symbol for an empty cross-level relation, not a subgroup. With \(K_{11}=N\), \(K_{00}=M\), \(K_{10}=X\), and \(K_{01}=Y\), the relation is
\[
(i,g)\mathrel{\rho}(j,h)\quad\Longleftrightarrow\quad gh^{-1}\in K_{ij},
\]
with membership in \(\varnothing\) always false. Containment of relations corresponds exactly to containment of all four parameters, treating \(\varnothing\) as below every subgroup.

Consequently the complete diagonal-relation count, congruence count, and DSC coefficient are
\[
\boxed{\begin{aligned}
D(G)&=|\operatorname{Diag}(S)|=\sum_{N\le M}(1+I(N,M))^2,\\
C(G)&=|\operatorname{Cong}(S)|=|\mathcal N(G)|+\sum_{N\le M}1,\\
\chi(S)&=C(G)/D(G).
\end{aligned}}
\]
All sums run over **normal** subgroup intervals of \(G\). The congruences are precisely the configurations with both \(X,Y\) empty, or with \(N=M=X=Y\).

For a prime \(p\) and \(G=(C_p)^d\), let \({m\brack n}_p\) be a Gaussian binomial and \(\Sigma_p(t)=\sum_{j=0}^t {t\brack j}_p\). Then
\[
\begin{aligned}
D_p(d)&=\sum_{0\le n\le m\le d}{d\brack m}_p{m\brack n}_p(1+\Sigma_p(m-n))^2,\\
C_p(d)&=\Sigma_p(d)+\sum_{0\le n\le m\le d}{d\brack m}_p{m\brack n}_p.
\end{aligned}
\]
For each **fixed** prime \(p\), the exact quadratic-logarithmic decay rate is
\[
\boxed{\lim_{d\to\infty}\frac{\log_p\bigl(C_p(d)/D_p(d)\bigr)}{d^2}=-\frac16.}
\]
Thus enlarging only the group rank, while keeping the semilattice at two points, makes the fraction of diagonal relations that are congruences decay on a quadratic-exponential scale. For every prime \(p\), the rank-one coefficient is \(5/17\), and the rank-two value at \(p=2\) is \(17/110\). For \(G=S_3\), the coefficient is \(9/46\).

## Assumptions and scope
The semigroup multiplication signature is \((\cdot)\) only: neither the group inverse nor a separate semilattice operation is part of the algebraic signature being tested for relation compatibility. The group is finite, including the trivial group. The two levels are distinct and carry isomorphic full group fibres with identity connecting homomorphism. The classification is **not** asserted for infinite groups or for arbitrary strong semilattices of groups. The asymptotic fixes the prime while the vector-space rank grows.

## Proof
**1. Strata are controlled by normal subgroups.** For a diagonal compatible relation \(\rho\), let \(R_{ij}\subseteq G\times G\) be the group-coordinate pairs related between level \(i\) and level \(j\). Because \(\min(i,i)=i\), every nonempty \(R_{ij}\) is a finite subsemigroup of the group \(G\times G\), hence a subgroup. Both \(R_{11}\) and \(R_{00}\) contain the diagonal subgroup \(\Delta_G=\{(g,g):g\in G\}\).

A subgroup \(H\le G\times G\) containing \(\Delta_G\) is precisely
\[
H_L=\{(g,h):gh^{-1}\in L\}
\]
for a unique normal subgroup \(L\triangleleft G\): take \(L=\{g:(g,e)\in H\}\), multiply by diagonal elements to recover \(H\), and conjugate by \(\Delta_G\) to obtain normality. Accordingly \(R_{11}=H_N\) and \(R_{00}=H_M\) for uniquely determined normal subgroups \(N,M\). Multiplying a top–top related pair by the diagonal bottom-level identity pair puts the same group-coordinate pair in \(R_{00}\); thus \(N\le M\).

If \(R_{10}\) is nonempty then, as a subgroup, it contains \((e,e)\). Multiplying this pair by every top-level diagonal pair \((g,g)\in R_{11}\) shows \(\Delta_G\subseteq R_{10}\). Hence \(R_{10}=H_X\) for a unique normal subgroup \(X\). Multiplication of \(R_{11}\) by \((e,e)\in R_{10}\) gives \(N\le X\), and multiplication of \(R_{10}\) by the bottom-level diagonal identity gives \(X\le M\). Therefore either \(R_{10}=\varnothing\) or \(N\le X\le M\). The same argument gives the stated choice of \(Y\) for \(R_{01}\).

**2. Every allowed configuration works.** Fix normal subgroups \(N\le M\), and select \(X,Y\) as stated. The four strata define a reflexive relation. Products of two pairs have the level pair obtained by taking minima coordinatewise. Group differences of products belong to the product of the corresponding normal subgroups: for \((g,h)\in H_A\), \((u,v)\in H_B\), write \(gh^{-1}\in A\), \(uv^{-1}\in B\); then \((gu)(hv)^{-1}=g(uv^{-1})g^{-1}(gh^{-1})\in BA\). The nesting \(N\le X,Y\le M\) ensures compatibility in each of the sixteen level-pair combinations: the two diagonal strata multiply within themselves; the top diagonal acts on either crossing stratum; any product involving the bottom diagonal and a crossing stratum lands in the bottom diagonal; and opposite crossings multiply into the bottom diagonal. Empty strata create no additional products. All choices therefore produce diagonal subsemigroups. Uniqueness of the four strata yields the classification and the stated containment order.

**3. Which relations are congruences?** If both crossings are empty, symmetry and transitivity hold separately on the two group levels: \(H_N\) and \(H_M\) are equivalences, and compatibility was proved above. If at least one crossing is nonempty, symmetry forces both nonempty and \(X=Y\). Transitivity between a top element, a bottom element, and a second bottom element forces \(M\le X\); thus \(X=M\). Transitivity between two top elements via a bottom element forces \(X\le N\). Coupled with \(N\le X\le M\), these give \(N=M=X=Y\). Conversely such a configuration identifies matching cosets across both levels and is a congruence. Summing the independent choices \(X,Y\) gives the \((1+I)^2\) diagonal count; the two congruence families give the displayed congruence count.

**4. Elementary abelian enumeration.** For \(G=(C_p)^d\), all subgroups are normal and are the \(\mathbb F_p\)-subspaces of a \(d\)-dimensional vector space. There are \({d\brack m}_p{m\brack n}_p\) nested pairs \(N\le M\) with \(\dim N=n\), \(\dim M=m\). Their interval is the subspace lattice of \(M/N\), hence has exactly \(\Sigma_p(m-n)\) members. This gives both exact Gaussian formulas.

**5. Quadratic-exponential rate.** For each fixed prime, there exists a finite constant \(B_p\ge1\), independent of \(d,k\), such that
\[
p^{k(d-k)}\le {d\brack k}_p\le B_p p^{k(d-k)}.
\]
This follows directly from the Gaussian product formula, with \(B_p=\prod_{j\ge1}(1-p^{-j})^{-1}\). Consequently
\[
p^{\lfloor t^2/4\rfloor}\le\Sigma_p(t)\le B_p(t+1)p^{t^2/4}.
\]
Write \(a=n\), \(b=m-n\), \(c=d-m\), so \(a+b+c=d\). The exponent of a summand in \(D_p(d)\), to within polynomial factors in \(d\), is
\[
ab+ac+bc+\frac{b^2}{2}=\frac{d^2-a^2-c^2}{2}\le\frac{d^2}{2}.
\]
The single choice \(N=0,M=G\) supplies the matching lower bound \((1+\Sigma_p(d))^2\ge p^{d^2/2-O(1)}\), so \(\log_p D_p(d)=d^2/2+O(\log(d+1))\). For the congruence count, the flag summands have exponent \(ab+ac+bc\le d^2/3\); taking \(a,b,c\) as equal as possible attains \(d^2/3-O(1)\). The additional \(\Sigma_p(d)\) term has logarithmic exponent at most \(d^2/4+O(\log(d+1))\). Therefore \(\log_p C_p(d)=d^2/3+O(\log(d+1))\). Subtracting proves the limiting exponent \(-1/6\).

## Verification
The accompanying standalone `checker.py` implements finite group multiplication, subgroup/normal-subgroup enumeration, and relation multiplication from scratch. It independently enumerates **every** compatible reflexive relation by closure-search for the trivial group, \(C_2\), \(C_3\), and \(C_2\times C_2\). In each case the exhaustive set agrees exactly with the predicted normal-subgroup-interval family. For \(S_3\), it verifies closure and the congruence test for all 46 predicted relations but does **not** enumerate all possible relations independently. It also evaluates the Gaussian formulas for primes \(2,3,5\) and dimensions \(1\) through \(5\). Running `python3 checker.py` produces `VERIFY_OK`. These finite checks test the proof and the formulas; they are not proofs for arbitrary groups or ranks.

## Relationship to prior work
Barber and Ruškuc introduced the DSC coefficient and, in Section 4 of their February 2026 preprint, constructed an injective **family** of diagonal subsemigroups on general finite Clifford semigroups, explicitly observing that it need not be exhaustive. They proved the bound \(\chi(S)\le\chi(E(S))\), not the complete two-level direct-product formula above. For \(G=C_p\), their kernel-and-trace construction provides twelve relations in this setting, whereas the complete count here is seventeen. Their Rees matrix classification concerns a different semigroup class. Their earlier study of diagonal subsemigroups establishes qualitative DSC criteria but not this normal-subgroup-interval count. General congruence-pair theory accounts for the congruence portion of the theorem; that portion alone does not determine all reflexive compatible relations.

## Limitations
The result is restricted to the two-level direct product with **identity** connecting group homomorphism. General nontrivial connecting maps, more semilattice levels, and infinite groups are not classified. The quadratic-exponential limit assumes fixed prime \(p\) and increasing rank; it does not make uniform claims when \(p\) also grows. The literature comparison is a best-knowledge mathematical overlap check, not a guarantee of historical priority: older treatments of compatible relations on strong semilattices of groups might encode an equivalent classification.

## References
1. C. Barber and N. Ruškuc, *Comparing numbers of diagonal subsemigroups and congruences for semigroups*, arXiv:2602.17286v1 (first posted 19 February 2026), especially Section 4; revised version arXiv:2602.17286v2, https://arxiv.org/html/2602.17286.
2. C. Barber and N. Ruškuc, *Semigroup congruences and subsemigroups of the direct square*, Bulletin of the Australian Mathematical Society 113 (2026), 123–134; https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/semigroup-congruences-and-subsemigroups-of-the-direct-square/908B89A485FCB609DF3254EF1E40A537.
3. J. M. Howie, *Fundamentals of Semigroup Theory*, Oxford University Press, 1995, standard background on normal subgroup/congruence pairs (not relied upon for the diagonal-relation classification).
