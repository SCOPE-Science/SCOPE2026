# Three-way temporal information and sharp observation horizons in Rule 90

## Finding

Let \(F\) be elementary binary cellular automaton Rule 90, \((Fx)_i=x_{i-1}+x_{i+1}\pmod 2\), acting on \(\{0,1\}^{\mathbb Z}\). Let \(X\) be sampled from the fair independent Bernoulli measure and let \(Y_r(j)=(F^jX)_r\). Choose arbitrary distinct integers \(a<b<c\), and define \(s=b-a\), \(t=c-a\), \(g=\gcd(s,t)\), and \(h=t-g\).

For **every** integer \(n\ge1\), the joint word \(((Y_a(j),Y_b(j),Y_c(j)))_{0\le j<n}\) is uniform on an explicitly described binary linear space of dimension
\[
\boxed{3n-\max\{0,n-h\}.}
\]
Each one-site temporal process is a sequence of independent fair bits; every **pair** of the three entire temporal processes is independent. Nevertheless their finite-block total correlation, in bits, is exactly
\[
\boxed{H(Y_a[0,n))+H(Y_b[0,n))+H(Y_c[0,n))-H(Y_{a,b,c}[0,n))=\max\{0,n-h\}.}
\]
The **first** dependent three-site block has time length exactly \(h+1\). The joint infinite temporal trace is a one-sided shift of finite type with a complete single parity-check rule of memory \(h\) and entropy \(2\log 2\) per time step.

An explicit complete parity relation is as follows. In \(\mathbb F_2[u]\), define \(P_0=0\), \(P_1=u\), and \(P_{k+1}=uP_k+P_{k-1}\) for \(k\ge1\). Define three *polynomials*
\[
A=P_{t-s}/P_g,\qquad B=P_t/P_g,\qquad C=P_s/P_g.
\]
These quotients exist exactly in \(\mathbb F_2[u]\). If \(E\) is forward shift in time, the entire joint trace language consists **precisely** of the triples obeying
\[
\boxed{A(E)Y_a(j)+B(E)Y_b(j)+C(E)Y_c(j)=0\quad(j=0,1,2,\ldots),}
\]
where sums and coefficients are over \(\mathbb F_2\). All three coefficients are nonzero, and their largest degree is exactly \(h\).

## Assumptions and scope

Sites are arbitrary *integers* satisfying \(a<b<c\); the initial spatial configuration is sampled using independent fair Bernoulli bits on the full *bi-infinite* binary shift. The rule and all algebra are over \(\mathbb F_2\), and time is \(j\in\mathbb N_0\). Shannon entropies in the finite-block identities are measured in bits; topological entropy is in natural logarithms. The result is about three **temporal sensors**, not three observations at one spatial time, and does not assert independence for four sensors or for other cellular automata.

## Proof

**1. Polynomial representation.** Write \(L=\mathbb F_2[z,z^{-1}]\), set \(u=z+z^{-1}\), and let \(R=\mathbb F_2[u]\). The linear form giving \(Y_r(j)\) on the initial configuration is \(z^ru^j\in L\). Since \(z^2=uz+1\) and \(z^{-1}=u+z\), every Laurent polynomial is an \(R\)-linear combination of \(1,z\). These elements are independent: if \(Q(u)+zT(u)=0\), conjugating by \(z\mapsto z^{-1}\) and adding gives \(uT(u)=0\), hence \(T=Q=0\). Thus \(L\) is free over \(R\) with basis \((1,z)\).

**2. The unique primitive relation.** For any two different spatial sites \(i,j\), the determinant in this basis of the two columns \(z^i,z^j\) equals \(P_{|j-i|}/u\), up to a unit (the sign is irrelevant in characteristic two). To verify this identity, multiply both columns by \(z^{-i}\), which has determinant one, and use \(z^k+z^{-k}=P_k(u)\), together with \(z^{-1}=u+z\). In particular, the determinant never vanishes for \(i\ne j\), so any two sensor-column families are \(R\)-independent.

For the three sites, the signed-minor kernel vector is \((P_{t-s},P_t,P_s)\). Furthermore,
\[
\gcd_R(P_s,P_t)=P_g.
\]
Indeed, \(P_k(z+z^{-1})=z^{-k}(z^{2k}+1)\), and the polynomial Euclidean algorithm gives \(\gcd(z^{2s}+1,z^{2t}+1)=z^{2g}+1\). Because the Laurent inclusion of \(R\) is saturated for divisibility by an \(R\)-polynomial (the basis \(1,z\) above), this identity descends to the stated gcd in \(R\). Equivalently, the Euclidean identity \(\gcd(P_s,P_t)=P_{\gcd(s,t)}\) follows by the standard recurrence of the binary Dickson polynomials. The remaining polynomial \(P_{t-s}\) is divisible by \(P_g\) because \(g\mid(t-s)\).

Therefore \((A,B,C)=(P_{t-s}/P_g,P_t/P_g,P_s/P_g)\) has gcd one and spans the *entire polynomial relation module*: if \((U,V,W)\) is a syzygy, the rank-two condition makes it a rational multiple of \((A,B,C)\). Bézout's identity for the three coprime coefficients forces that multiplier to lie in \(R\). Conversely, every polynomial multiple is a syzygy.

**3. Sharp finite-length rank.** The \(3n\) observations have a linear dependence precisely when three polynomials \(U,V,W\) of degree at most \(n-1\) satisfy \(Uz^a+Vz^b+Wz^c=0\). By Step 2, \((U,V,W)=D(A,B,C)\). The polynomials \(P_k\) have degree \(k\), so the maximum degree among \(A,B,C\) is \(\deg B=t-g=h\). Consequently \(D\) may have degree at most \(n-1-h\). The dimension of the dependence space is \(\max\{0,n-h\}\), since its basis is given by \(D=1,u,\ldots,u^{n-h-1}\) when \(n>h\). Thus the observation rank is exactly \(3n-\max\{0,n-h\}\), with no finite-enumeration hypothesis.

**4. Exact joint law and independent pairs.** Every finite family of these observations is a linear image of finitely many initial fair independent bits, and a linear image of a uniform binary vector is uniform on its image. By Step 3 the joint law is uniform on a subspace of the claimed size. A single sensor's forms \(z^ru^j\) are independent because \(R\) is a domain, and two sensors' forms are independent because their two basis columns have nonzero determinant. Hence every single trace and every pair of whole traces are respectively iid fair and mutually independent; subtracting ranks yields the total-correlation formula.

**5. Whole temporal language and entropy.** The one-step parity equation above is a syzygy and therefore holds on every orbit. Conversely, if an infinite triple temporal sequence satisfies all such equations, then every finite prefix is orthogonal to every bounded-degree syzygy by Step 2 and hence lies in the finite observation image. The preimage cylinder sets in the compact full shift are nonempty, closed, and nested; compactness supplies an initial configuration realizing the entire sequence. Thus the parity equation exactly presents the trace subshift. Its window has \(h+1\) times and, by Step 3, every shorter temporal block is allowed, giving the sharp onset. The word count is \(2^{3n-\max(0,n-h)}\), whence its entropy rate is \(\lim_{n\to\infty}n^{-1}\log\#\mathcal L_n=2\log2\).

## Verification

A standalone exact-arithmetic Python 3 program, `verify.py`, independently represents the spatial-time observation forms as Laurent-polynomial coefficient vectors and performs Gaussian elimination over \(\mathbb F_2\). It tests all 119 separation pairs \(1\le s<t\le16\) with \(s\le14\) and all \(1\le n\le11\) (1,309 ranks). Separately it checks the binary-polynomial gcd and the predicted primitive-relation degrees. These finite checks are independent corroboration; Steps 1–5 prove the unrestricted statement. Run: `python3 verify.py`.

## Relationship to prior work

The algebraic representation of additive cellular automata is classical, notably in Wolfram (1983) and Martin–Odlyzko–Wolfram (1984). Cervelle–Formenti–Guillon (2007) give a general account of cellular-automaton trace subshifts, principally the realizability of specified trace shifts. Rosas and collaborators (2018) discuss synergistic information in Rule 90 under a different, primarily spatial information-theoretic setup. Rowland–Yassawi study automatic sequences obtained as columns of linear cellular automata. None of the inspected available statements supplies this *all-spacings three-temporal-sensor finite-block rank law*, its \(\gcd\)-controlled first obstruction, and complete parity-check presentation. These are comparisons of statements rather than claims of exhaustive historical novelty.

## Limitations

The theorem concerns fair Bernoulli initial data, three distinct sites, Rule 90, and forward-time observations. Uniformity is essential for the entropy interpretation, but not for the algebraic language/rank calculation. The work does not classify four-site dependencies or other rules. Prior linear-coding literature may contain an equivalent reformulation not identified here; one relevant manuscript's full publisher text was inaccessible. No independent scientific audit has been performed.

## References

1. S. Wolfram, *Statistical mechanics of cellular automata*, Rev. Mod. Phys. 55 (1983), 601–644; doi:10.1103/RevModPhys.55.601.
2. O. Martin, A. Odlyzko, S. Wolfram, *Algebraic Properties of Cellular Automata*, Commun. Math. Phys. 93 (1984), 219–258; doi:10.1007/BF01223745.
3. J. Cervelle, E. Formenti, P. Guillon, *Sofic Trace Subshift of a Cellular Automaton*, arXiv:math/0703241 (2007).
4. F. Rosas et al., *An Information-Theoretic Approach to Self-Organisation*, Entropy 20 (2018), 793; doi:10.3390/e20100793.
5. E. Rowland, R. Yassawi, *A characterization of p-automatic sequences as columns of linear cellular automata*, arXiv:1209.6008.
