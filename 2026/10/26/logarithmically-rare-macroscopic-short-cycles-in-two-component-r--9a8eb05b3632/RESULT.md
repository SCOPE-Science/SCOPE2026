# Logarithmically rare macroscopic short cycles in two-component random mappings

## Finding

Let \(f:[n]\to[n]\) be a uniformly random mapping, conditioned to have exactly two weakly connected components. Every such component contains one directed cycle. Write \(K_n\) for the total number of vertices on those two cycles and \(S_n\) for the shorter cycle length. The following assertions hold.

**Exact joint law.** For \(2\le k\le n\) set
\[
a_{n,k}=\frac{(n)_k}{n^k},\qquad H_j=\sum_{i=1}^j\frac1i,\qquad Z_n=\sum_{k=2}^n a_{n,k}H_{k-1}.
\]
Then \(\Pr(M_n=2)=Z_n/n\), where \(M_n\) is the component count, and
\[
\Pr(K_n=k,S_n=s\mid M_n=2)=\frac{a_{n,k}}{Z_n}\begin{cases}
\frac1s+\frac1{k-s},&1\le s<k/2,\\[2pt]
\frac1s,& k=2s.
\end{cases}
\]

**Macroscopic boundary-layer law.** Put \(I_0=\int_0^\infty e^{-x^2/2}\,dx=\sqrt{\pi/2}\). On the open region \(\Omega=\{(x,y):x>0,\ 0<y<x/2\}\), the locally finite measures
\[
(\log n)\Pr\!\left(\bigl(K_n/\sqrt n,S_n/\sqrt n\bigr)\in\cdot\mid M_n=2\right)
\]
converge vaguely to the measure with density
\[
\boxed{\frac{2}{I_0}e^{-x^2/2}\left(\frac1y+\frac1{x-y}\right),\qquad (x,y)\in\Omega.}
\]
In particular, for every fixed \(a>0\),
\[
\boxed{\lim_{n\to\infty}(\log n)\Pr(S_n\ge a\sqrt n\mid M_n=2)
=\frac{2}{I_0}\int_{2a}^{\infty}e^{-x^2/2}\log\!\left(\frac{x-a}{a}\right)\,dx.}
\]
This limit is finite and strictly positive: a shorter cycle of macroscopic size occurs with probability of order \(1/\log n\).

**All positive power moments.** For every fixed real \(q>0\),
\[
\boxed{\mathbb E[S_n^q\mid M_n=2]\sim \frac{2I_q\mu_q}{\log n}\,n^{q/2},\quad
I_q=\int_0^{1/2}\frac{t^{q-1}}{1-t}\,dt,\quad
\mu_q=\frac{2^{q/2}\Gamma((q+1)/2)}{\sqrt\pi}.}
\]
Consequently,
\[
\mathbb E[S_n\mid M_n=2]\sim 2\log2\sqrt{\frac2\pi}\frac{\sqrt n}{\log n},\qquad
\operatorname{Var}(S_n\mid M_n=2)\sim(2\log2-1)\frac n{\log n}.
\]
For comparison, the typical logarithmic scale is much smaller: jointly,
\[
\left(K_n/\sqrt n,\ \log S_n/\log n\right)\ \xrightarrow{\mathrm d}\ (|G|,U/2),
\]
where \(G\) is standard Gaussian, \(U\) uniform on \([0,1]\), and they are independent. This last weak-scale statement follows from the classical conditional permutation-cycle law; the quantitative macroscopic boundary layer and moment constants are the focus here.

## Assumptions and scope

All \(n\ge2\) are integers. Every function from \([n]\) to itself has probability \(n^{-n}\). Loops are allowed; weakly connected components are defined in the underlying undirected functional graph. Every component contains exactly one directed cycle, including loops. No exclusions on self-maps, component sizes, or repeated cycle lengths are imposed. Statements concerning convergence hold as \(n\to\infty\), with \(q\) and \(a\) fixed. Logarithms are natural.

## Proof

**Step 1: exact decomposition.** Choose the cyclic set of size \(k\). For any specified permutation of its \(k\) points, the noncyclic vertices form a rooted forest directed toward those roots, with \(k n^{n-k-1}\) possible choices. Consequently the unconditional probability of \(K_n=k\) is \(a_{n,k}k/n\), and conditional on that event the permutation of cyclic vertices is uniform. The number of permutations on \(k\) points having precisely two cycles is the unsigned Stirling number \(\left[{k\atop2}\right]=(k-1)!H_{k-1}\). Hence
\[
\Pr(K_n=k,M_n=2)=\frac{a_{n,k}H_{k-1}}n.
\]
For \(s<k/2\), the number of permutations with cycle lengths \(s,k-s\) is \(k!/[s(k-s)]\); when \(k=2s\), it is \(k!/(2s^2)\). Divide by \((k-1)!H_{k-1}\) to obtain the displayed joint law and \(\Pr(M_n=2)=Z_n/n\). This accounts for the equal-length boundary without double counting.

**Step 2: core normalization.** With \(k=\lfloor x\sqrt n\rfloor\), \(a_{n,k}\to e^{-x^2/2}\). The elementary bound
\[
a_{n,k}=\prod_{j=0}^{k-1}\left(1-\frac jn\right)\le\exp\left(-\frac{k(k-1)}{2n}\right)
\]
provides Gaussian domination. As \(H_{k-1}=\log k+\gamma+o(1)\), Gaussian-dominated Riemann sums give
\[
Z_n\sim\frac12(\log n)\sqrt n\int_0^\infty e^{-x^2/2}\,dx
=\frac{I_0}{2}\sqrt n\log n.
\]
The same argument with a bounded continuous test function yields \(K_n/\sqrt n\Rightarrow |G|\) conditional on two components.

**Step 3: the rare-event measure.** For interior lattice points \(k\sim x\sqrt n\), \(s\sim y\sqrt n\), the exact joint mass is
\[
\frac{a_{n,k}}{Z_n}\left(\frac1s+\frac1{k-s}\right)
=\frac{2e^{-x^2/2}+o(1)}{I_0 n\log n}
\left(\frac1y+\frac1{x-y}\right).
\]
There are asymptotically \(n\,dx\,dy\) lattice pairs in a small rectangle. Summation against compactly supported continuous test functions in \(\Omega\) proves vague convergence. The equal-cycle diagonal contributes no macroscopic mass after multiplying by \(\log n\). For the tail \(s\ge a\sqrt n\), the same Gaussian bound makes the large-\(k\) region uniformly negligible; \(s\ge a\sqrt n\) also keeps the singularity at \(y=0\) away. The inner integral is
\[
\int_a^{x/2}\left(\frac1y+\frac1{x-y}\right)dy=\log\left(\frac{x-a}{a}\right),\quad x\ge2a,
\]
which proves the stated tail limit.

**Step 4: moments and nonuniform integrability.** Define the unnormalized conditional moment for a two-cycle permutation on \(k\) elements by
\[
F_q(k)=\sum_{1\le s<k/2}s^q\left(\frac1s+\frac1{k-s}\right)
+\boldsymbol1_{\{2\mid k\}}\left(\frac k2\right)^{q-1}.
\]
Its Riemann sum satisfies \(k^{-q}F_q(k)\to I_q\) for each \(q>0\). Indeed the summand near zero is bounded by \(C_qs^{q-1}\), and \(q>0\) makes the endpoint integrable; the possible equal-cycle correction is \(O(k^{q-1})\). Moreover \(F_q(k)\le C_q k^q\) uniformly. Therefore Gaussian domination and the normalization in Step 2 give
\[
\sum_{k=2}^n a_{n,k}F_q(k)\sim I_q n^{(q+1)/2}\int_0^\infty x^qe^{-x^2/2}\,dx.
\]
After division by \(Z_n\), the coefficient is \(2I_q/I_0\) times the integral, equal to \(2I_q\mu_q\), since \(\mu_q=I_0^{-1}\int_0^\infty x^qe^{-x^2/2}\,dx\). For \(q=1\), \(I_1=\log2\) and \(\mu_1=\sqrt{2/\pi}\). For \(q=2\), \(I_2=\log2-1/2\) and \(\mu_2=1\). The squared mean is \(O(n/(\log n)^2)\), negligible versus the second moment, proving the variance formula.

**Step 5: logarithmic-scale contrast.** For any \(0<b<1/2\), uniformly when \(k/\sqrt n\) stays in a fixed compact positive interval, the conditional formula gives
\[
\Pr(S_n\le n^b\mid K_n=k,M_n=2)=\frac{H_{\lfloor n^b\rfloor}+O(n^b/k)}{H_{k-1}}\longrightarrow2b.
\]
Combine this with tightness of \(K_n/\sqrt n\), asymptotic normalizer \(Z_n\), and bounded test functions to obtain the joint independent weak limit. Weak convergence on a logarithmic scale does not control the power moments: they come from the separately proved \(1/\log n\) macroscopic boundary layer.

## Verification

The included standalone `verify.py` independently exhausts all \(n^n\) mappings for \(2\le n\le6\), identifies cycles without any use of the counting formula, and exactly compares every \((K_n,S_n)\) stratum to the proposed rational law. It also computes finite conditional first and second moments from exact harmonic identities at sample sizes 1,000, 10,000, and 100,000 and compares normalized values with the predicted constants. The verifier completed with `VERIFY_OK`. These finite checks corroborate the proof but do not establish asymptotics; Steps 2–5 provide the unrestricted analytic arguments.

## Relationship to prior work

Arratia and Tavaré (1992), especially Section 6.A and equations (59)–(63), give the classical random-mapping core mixture with a uniform conditional permutation and a small-cycle Poisson approximation at lengths \(o(\sqrt n)\). Their Section 2.E treats smallest permutation cycle lengths without conditioning the total cycle count to equal two. Granville (2006) studies permutations conditioned on fixed cycle count; his logarithmic scale results cover the weak distributional interpretation above, which is **not** presented as a new standalone theorem. Arratia and Tavaré (1994) give general conditioning and moment frameworks for assemblies, including mappings, but their inspected results do not give the two-component shorter-cycle boundary intensity or its fixed positive-moment asymptotics. Finch (2022) analyzes cycles and components of random mappings and the fixed-component core scale. The new quantitative target is the precisely conditioned *macroscopic* short-cycle boundary-layer measure and its all-positive-power moments, for which convergence on logarithmic or sub-\(\sqrt n\) scales alone is insufficient. The exact finite joint formula is a specialization of classical mapping/permutation enumeration, and is included as a transparent starting point rather than claimed as a new enumeration principle.

## Limitations

The random mapping is uniform and the component count is conditioned to equal exactly two; no result is asserted for other fixed component counts, biased mappings, or derangements. The limiting boundary-layer measure is infinite near zero, so vague convergence cannot be promoted to probability-measure convergence. The all-power-moment theorem requires each exponent \(q>0\) fixed as \(n\to\infty\). The logarithmic-scale weak law does not imply the moment asymptotics. Historical priority for exact mixed conditional moment constants is not independently certified; classical general generating-function or fixed-count enumerations could conceivably yield them by an unlocated specialization.

## References

1. R. Arratia and S. Tavaré, “Limit Theorems for Combinatorial Structures via Discrete Process Approximations,” *Random Structures & Algorithms* **3** (1992), 321–345, DOI:10.1002/rsa.3240030310. Author-hosted full text: https://www.columbia.edu/cu/simontavare/STpapers-pdf/AT92b.pdf.
2. A. Granville, “Cycle Lengths in a Permutation Are Typically Poisson,” *Electronic Journal of Combinatorics* **13** (2006), #R107, DOI:10.37236/1133. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r107/pdf/.
3. S. R. Finch, “Components and Cycles of Random Mappings,” arXiv:2205.05579, first posted 2022-05-11. Full text: https://arxiv.org/pdf/2205.05579.
4. S. Tavaré, “A Note on the Screaming Toes Game,” *Journal of Applied Probability* **59** (2022), 118–130. Author-hosted full text: https://www.columbia.edu/cu/simontavare/STpapers-pdf/t20a.pdf.
5. R. Arratia and S. Tavaré, “Independent Process Approximations for Random Combinatorial Structures,” *Advances in Mathematics* **104** (1994), 90–154. Open manuscript: https://arxiv.org/pdf/1308.3279.
