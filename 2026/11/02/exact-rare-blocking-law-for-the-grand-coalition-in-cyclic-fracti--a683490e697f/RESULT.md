# Exact rare-blocking law for the grand coalition in cyclic fractional hedonic games

## Finding

For every integer \(n\geq 3\), let \(C_n\) be the simple undirected cycle on \(n\) labeled agents. Each agent assigns value \(1\) to each of its two cycle neighbors and \(0\) to every other agent. For any nonempty coalition \(S\), its utility is the number of the agent's neighbors in \(S\), divided by \(|S|\). Start with the grand-coalition partition \(\pi=\{V(C_n)\}\), and say that \(S\) **blocks** when *every* member strictly improves by joining \(S\).

The number \(B_n\) of blocking coalitions is exactly
\[
B_n=\sum_{s=2}^{\lfloor(n-1)/2\rfloor}
\ \sum_{r=1}^{\lfloor s/2\rfloor}
\frac{n}{r}\binom{s-r-1}{r-1}\binom{n-s-1}{r-1}.
\]
The empty sum is zero. Equivalently, blocking coalitions are precisely the vertex subsets of cardinality strictly less than \(n/2\) that induce no isolated vertices in the cycle. In particular \(B_3=B_4=0\), while \(B_n>0\) for every \(n\ge5\).

For a uniform random subset of all \(2^n\) subsets, the exact blocking probability is \(\varepsilon_n=B_n/2^n\). As \(n\to\infty\), with fixed parity,
\[
\varepsilon_n\sim\frac{1}{\sqrt{2\pi n}}
\left(\frac{\sqrt3}{2}\right)^n
\begin{cases}
3\sqrt3,&n\text{ even},\\
6,&n\text{ odd}.
\end{cases}
\]
Consequently \(\lim_{n\to\infty}\varepsilon_n^{1/n}=\sqrt3/2\). For uniform sampling of **nonempty** coalitions, replace the denominator \(2^n\) by \(2^n-1\); the same asymptotic holds. This is an exact probability for the specified partition, not a minimum across all partitions.

## Assumptions and scope

The graph is the labeled, unweighted, undirected cycle \(C_n\), including the triangle when \(n=3\). Self-value is zero. Utility is the original fractional-hedonic normalization by the full coalition cardinality, including the agent itself. Comparison is strict for **every** member of a deviating coalition; weak blocking and strict-core blocking are different notions and not claimed here. All nonempty subsets, not necessarily connected, are admissible deviations. Cycles have no other positive valuation edges. The sampling law is uniform over all subsets (or, when explicitly stated, over nonempty subsets).

## Proof

**1. Characterization.** The baseline grand-coalition utility is \(2/n\) for each agent. For a deviation \(S\) with \(s=|S|\), agent \(i\in S\) gets \(d_S(i)/s\), where \(d_S(i)\in\{0,1,2\}\) is the degree of \(i\) in the induced subgraph \(C_n[S]\). Thus \(S\) blocks if and only if \(n d_S(i)>2s\) for every \(i\in S\). If \(s<n/2\), this holds exactly when every vertex of \(S\) has an included neighbor. If \(n/2\le s<n\), it would require \(d_S(i)=2\) for all selected vertices. A nonempty proper subset of a connected cycle cannot be closed under both neighbors, so none can qualify. The whole vertex set has unchanged utility and does not block. This proves the asserted characterization, including both equality boundaries.

**2. Exact run count.** When \(2\le s<n/2\), mark included cycle vertices by \(1\) and excluded ones by \(0\). Because neither symbol occupies the whole cycle, a valid word has \(r\ge1\) cyclic runs of ones, each of length at least \(2\), separated by \(r\) zero runs, each of length at least \(1\). The number of ordered compositions of \(s\) into \(r\) parts at least \(2\) is \(\binom{s-r-1}{r-1}\); the number of ordered compositions of \(n-s\) into \(r\) positive parts is \(\binom{n-s-1}{r-1}\). Choose the start of a distinguished one-run among \(n\) labeled cycle vertices; every subset is counted once per one-run, namely \(r\) times. Hence the count for fixed \(s,r\) is \((n/r)\) times the two binomial factors. Summing gives \(B_n\). A size-two edge blocks exactly when \(n>4\), proving the positivity cutoff.

**3. Transfer-matrix generating function.** Let \(a_{n,s}\) count all cyclic binary words on \(n\) labeled sites with exactly \(s\) ones and with no isolated one-runs. Include the all-zero and all-one words. Use the three states \(0\), first \(1\) of a run, and later \(1\) of a run. If each newly entered \(1\) has weight \(z\), the transition matrix is
\[
M(z)=\begin{pmatrix}1&z&0\\0&0&z\\1&0&z\end{pmatrix},
\qquad Z_n(z)=\operatorname{tr}(M(z)^n)=\sum_{s=0}^n a_{n,s}z^s.
\]
For every \(n\ge3\), every admissible cyclic binary word has a unique cyclic assignment of states; the all-zero and all-one words each contribute once. The characteristic polynomial is
\[
F(\lambda,z)=\lambda(\lambda-1)(\lambda-z)-z^2.
\]
Consequently \(Z_0=3\), \(Z_1=1+z\), \(Z_2=1+z^2\), and
\[
Z_n=(1+z)Z_{n-1}-zZ_{n-2}+z^2Z_{n-3}\qquad(n\ge3).
\]
In particular the exact alternative computation is \(B_n=\sum_{s=0}^{\lfloor(n-1)/2\rfloor}a_{n,s}-1\), subtracting the all-zero word.

**4. Sharp asymptotic and parity constants.** Fix \(z_0=3/4\). The positive matrix \(M(z_0)\) is primitive. Its simple Perron root is \(\lambda_0=3/2\), since
\[
F(\lambda,z_0)=\frac1{16}(2\lambda-3)(8\lambda^2-2\lambda+3).
\]
The other roots have modulus \(\sqrt6/4<3/2\). By implicit differentiation of \(F(\lambda(z),z)=0\), at \(z_0\) one finds \(\lambda'=1\), \(\lambda''=2/9\). Hence the first two logarithmic derivatives are
\[
\mu=\frac{z_0\lambda'(z_0)}{\lambda_0}=\frac12,
\qquad \sigma^2=\left.(z\partial_z)^2\log\lambda(z)\right|_{z=z_0}=\frac13.
\]
We give the local coefficient argument rather than treating a numerical fit as a proof. Fourier inversion on the circle \(|z|=z_0\) gives
\[
a_{n,s}z_0^s=\frac1{2\pi}\int_{-\pi}^{\pi}Z_n(z_0e^{i\theta})e^{-is\theta}\,d\theta.
\]
The only angle where \(M(z_0e^{i\theta})\) can have spectral radius \(\lambda_0\) is \(\theta=0\): equality in the Perron triangle bound forces every positive edge phase to be a common eigenphase times a vertex-potential difference. The \(0\to0\) self-loop forces the common eigenphase to be one, and the \(2\to2\) self-loop then forces \(e^{i\theta}=1\). Thus there is a uniform spectral gap away from \(0\). Analytic perturbation of the simple Perron root near zero yields
\[
\log\frac{\lambda(z_0e^{i\theta})}{\lambda_0}
=i\mu\theta-\frac{\sigma^2\theta^2}{2}+O(|\theta|^3).
\]
The remaining two eigenvalues stay strictly smaller in modulus. Splitting the Fourier integral into a shrinking Gaussian neighborhood and its complement now proves, uniformly for integer \(s-n/2=O(1)\),
\[
a_{n,s}\sim\frac{\lambda_0^n z_0^{-s}}{\sqrt{2\pi\sigma^2 n}}.
\]
The identical integral bound without its oscillatory factor also gives the **uniform** inequality \(a_{n,s}z_0^s\le C\lambda_0^n/\sqrt n\) for every \(s\), with a constant independent of \(n,s\). This supplies the domination needed for the remaining sum.

Set \(s_{\max}=\lfloor(n-1)/2\rfloor\) and \(\delta_n=n/2-s_{\max}\), equal to \(1\) for even \(n\) and \(1/2\) for odd \(n\). For fixed \(k\ge0\), substitute \(s=s_{\max}-k\) into the local coefficient asymptotic. Since \(z_0<1\), the uniform coefficient bound dominates the normalized terms by a summable geometric sequence \(O(z_0^k)\). Dominated convergence and the fact that the all-zero word is exponentially negligible imply
\[
B_n\sim \frac{\lambda_0^n z_0^{-n/2}}{\sqrt{2\pi\sigma^2n}}
\frac{z_0^{\delta_n}}{1-z_0}
=\frac{4(3/4)^{\delta_n}}{\sqrt{2\pi n/3}}\,3^{n/2}.
\]
Dividing by \(2^n\) and evaluating the two values of \(\delta_n\) yields precisely the displayed parity-dependent constants. The limit of the \(n\)-th root follows.

## Verification

Run `python3 verify_cycle_core.py` with Python 3.9 or later. It compares the exact run formula against direct rational-inequality tests of every selected member for all nonempty subsets for \(3\le n\le18\), and separately against the trace-polynomial recurrence for \(3\le n\le150\). It also prints four finite-size ratios to the proved asymptotic for illustration. The reported result is `PASS: 16 direct-payoff and 148 matrix-versus-run exact cases`. Direct enumeration is finite evidence only; the proof above establishes the all-size identities and asymptotics.

## Relationship to prior work

Aziz et al., *Fractional Hedonic Games*, define the symmetric binary valuation model and discuss core versus strict-core failure on \(C_5\); their cycle example does not count all strictly blocking coalitions or give their probability. Fioravanti et al., *\(\varepsilon\)-fractional Core Stability in Hedonic Games* (2023), introduce the uniform-coalition blocking probability as a quantitative stability measure and prove general computable bounds. Their general-purpose existence algorithm and guarantees do not specify the blocking law of the grand partition on cycle graphs. Fanelli et al. (2021) analyze size- and improvement-factor relaxations, and Demeulemeester and Peters (2024) refine that factor relationship; neither result supplies a probability distribution or the sharp cycle-specific exponential base. This theorem does not claim invention of cyclic run-composition enumeration or the finite-state Fourier method themselves; its contribution is the exact blocking equivalence and its sharp probabilistic consequence in this game.

## Limitations

This is a theorem for the **grand coalition only**. It does not assert that the grand coalition minimizes the blocking probability or maximizes welfare; indeed, known core-stable partitions exist on cycles. It does not cover weighted edges, directed valuations, weak-blocking deviations, a nonuniform sampling distribution, or graphs other than simple cycles. The combinatorial transfer-matrix identity may be known independently in the enumeration literature; priority is assessed specifically for its application to strict fractional-hedonic core blocking and the exact parity-sensitive probability. Further unindexed priority risk remains.

## References

1. S. Fioravanti, M. Flammini, B. Kodric, and G. Varricchio, *\(\varepsilon\)-fractional Core Stability in Hedonic Games*, NeurIPS 2023; first arXiv posting 2023-11-18, https://arxiv.org/abs/2311.11101 .
2. H. Aziz, F. Brandl, F. Brandt, P. Harrenstein, M. Olsen, and D. Peters, *Fractional Hedonic Games*, preprint 2017, https://arxiv.org/abs/1705.10116 .
3. A. Fanelli, G. Monaco, and L. Moscardelli, *Relaxed Core Stability in Fractional Hedonic Games*, IJCAI 2021, https://ijcai.org/proceedings/2021/26 .
4. T. Demeulemeester and J. Peters, *Quantifying Core Stability Relaxations in Hedonic Games*, first arXiv posting 2024-12-02, https://arxiv.org/abs/2412.01666 .
