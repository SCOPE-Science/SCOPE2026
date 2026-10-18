# Gaussian cutoff profile for adjacent-edge heat-bath on a binary cycle

## Finding

For each integer \(n\ge3\), consider the chain on \(\{0,1\}^{n}\) which, at each discrete step, chooses an edge uniformly from the \(n\) edges of the cyclic graph \(C_n\), independently replaces both endpoint bits by independent fair bits, and leaves every other bit unchanged. Write \(P_{n,t}^{x}\) for the law at step \(t\) from deterministic state \(x\), and \(\pi_n\) for the uniform measure on the cube. This chain is irreducible, aperiodic, reversible, and has stationary distribution \(\pi_n\).

For any fixed real \(c\), and for all sufficiently large \(n\) that the integer below is nonnegative, put
\[
 t_n(c)=\left\lfloor\frac n4\log n+cn\right\rfloor,\qquad
 b_{n,c}=\left(1-\frac2n\right)^{t_n(c)},\qquad
 a_c=e^{-2c}.
\]
Let \(G_{n,c}^{x}\) be the product distribution of independent bits, each equal to its initial bit \(x_i\) with probability \((1+b_{n,c})/2\), and different from \(x_i\) with probability \((1-b_{n,c})/2\). Then the *densities* satisfy the strong approximation
\[
 \left\|\frac{dP_{n,t_n(c)}^{x}}{d\pi_n}-
              \frac{dG_{n,c}^{x}}{d\pi_n}\right\|_{L^2(\pi_n)}\longrightarrow0,
\]
uniformly over deterministic starting states \(x\). In particular, the total-variation distance has the exact Gaussian cutoff profile
\[
 \sup_{x}\|P_{n,t_n(c)}^{x}-\pi_n\|_{\mathrm{TV}}
 \longrightarrow 2\Phi\!\left(\frac{e^{-2c}}2\right)-1,
\]
where \(\Phi\) is the standard normal distribution function. Simultaneously,
\[
 \chi^2(P_{n,t_n(c)}^{x}\,\|\,\pi_n)
 \longrightarrow \exp(e^{-4c})-1.
\]
Thus the total-variation cutoff location is \((n/4)\log n\) and its window is of order \(n\). More strongly, although the selected edges overlap, near cutoff their effect on the *entire joint law* is asymptotically the same in \(L^2(\pi_n)\) as independently refreshing each coordinate with the corresponding mean decay.

## Assumptions and scope

An edge is chosen independently on each step, uniformly among all consecutive vertex pairs including the closing edge. Upon selection, each endpoint is resampled independently from \(\operatorname{Bernoulli}(1/2)\), even if it happens to retain its former value. The starting configuration is deterministic. Total variation is \(\|\mu-\nu\|_{\mathrm{TV}}=\frac12\sum_y|\mu(y)-\nu(y)|\). Chi-square divergence is \(\chi^2(\mu\|\pi)=\sum_y\pi(y)(d\mu/d\pi(y)-1)^2\). Every limit is along integers \(n\to\infty\), at a fixed real window parameter \(c\). No assertion is made for interacting spins, nonuniform edge weights, larger blocks, or a window parameter diverging with \(n\).

## Proof

**1. Exact spectral representation.** Identify cube points with vectors over \(\mathbb F_2\), and, for \(S\subseteq[n]\), let the Walsh character be
\[
 \chi_S(y)=(-1)^{\sum_{i\in S}y_i}.
\]
Refreshing an edge annihilates a character if at least one endpoint belongs to \(S\), and otherwise leaves it unchanged. Consequently the eigenvalue is
\[
 \lambda_n(S)=1-\frac{|\partial_E S|}{n},
\]
where \(\partial_E S\) denotes the set of cycle edges having at least one endpoint in \(S\). This is an incident-edge set, not the usual crossing-edge boundary. The Walsh characters form an orthonormal basis of \(L^2(\pi_n)\). Starting from the all-zero vector therefore gives
\[
 f_{n,t}(y):=\frac{dP^0_{n,t}}{d\pi_n}(y)
 =\sum_{S\subseteq[n]}\lambda_n(S)^t\chi_S(y).
\]
For \(1\le |S|=k<n\), write \(r(S)\) for the number of nonempty cyclic runs of consecutive vertices in \(S\). Exactly \(k-r(S)\) cycle edges have both endpoints in \(S\). Since every vertex is incident to two edges, \(|\partial_E S|=2k-(k-r(S))=k+r(S)\). Thus
\[
 \lambda_n(S)=1-\frac{k+r(S)}{n}.
\]
The full set has eigenvalue zero. Translation by the initial state \(x\) transfers every conclusion for start zero to every deterministic start.

**2. Exact run multiplicities.** For \(1\le r\le\min(k,n-k)\), the number of \(k\)-element proper subsets with \(r\) cyclic runs equals
\[
 N(n,k,r)=\frac nr\binom{k-1}{r-1}\binom{n-k-1}{r-1}.
\]
Indeed, point to a distinguished start of one of the \(r\) runs (there are \(n\) possible sites), specify positive compositions of the occupied and unoccupied lengths into \(r\) parts each, and divide by the \(r\) choices of the distinguished run. A useful uniform estimate is
\[
 N(n,k,r)\le\frac{n^r}{r!}\binom{k-1}{r-1}.
\]
The product-law density, for start zero, is
\[
 g_{n,t}(y)=\prod_{i=1}^n(1+b_{n,t}\chi_{\{i\}}(y))
 =\sum_{S\subseteq[n]}b_{n,t}^{|S|}\chi_S(y),
 \qquad b_{n,t}=(1-2/n)^t.
\]

**3. Negligible run collisions in \(L^2\).** Put \(w_{n,t}=e^{-2t/n}\), and take \(t=t_n(c)\). Then \(n w_{n,t}^2\to a_c^2\), \(w_{n,t}\to0\), and \(n b_{n,t}^2\to a_c^2\). For a proper set with \(r<k\), its eigenvalue is at most \(e^{-(k+r)/n}\); hence \(\lambda_n(S)^{2t}\le w_{n,t}^{k+r}\). Using the run bound and summing \(m=k-r\ge1\) yields
\[
 \begin{aligned}
 \sum_{S:\,|S|>r(S)}\lambda_n(S)^{2t}
 &\le\sum_{r\ge1}\frac{(nw_{n,t}^2)^r}{r!}
       \sum_{m\ge1}\binom{m+r-1}{r-1}w_{n,t}^m\\
 &=\exp\!\left(\frac{nw_{n,t}^2}{1-w_{n,t}}\right)
       -\exp(nw_{n,t}^2)\longrightarrow0.
 \end{aligned}
\]
(The sum on the left excludes the full set, whose eigenvalue is zero.) The corresponding nonisolated Fourier mass of the product density obeys
\[
 \sum_{S:\,|S|>r(S),\,S\ne[n]}b_{n,t}^{2|S|}
 \le\exp\!\left(\frac{nb_{n,t}^2}{1-b_{n,t}^2}\right)
       -\exp(nb_{n,t}^2)\longrightarrow0.
\]
Here \(|S|=r(S)\) characterizes sets with no adjacent occupied vertices, called isolated sets below.

**4. Isolated sets and Fourier-tail control.** For an isolated set of cardinality \(k\), \(r(S)=k\), and \(\lambda_n(S)=1-2k/n\). At any fixed positive integer \(k\),
\[
 \frac{(1-2k/n)^t}{(1-2/n)^{kt}}\longrightarrow1,
 \qquad N(n,k,k)\sim\frac{n^k}{k!},
\]
so its total squared coefficient discrepancy vanishes:
\[
 N(n,k,k)\big((1-2k/n)^t-b_{n,t}^k\big)^2\longrightarrow0.
\]
For arbitrary \(k\), the isolated eigenvalue and product Fourier masses have the summable bounds
\[
 N(n,k,k)(1-2k/n)^{2t}\le\frac{(nw_{n,t}^2)^k}{k!},
 \qquad N(n,k,k)b_{n,t}^{2k}\le\frac{(nb_{n,t}^2)^k}{k!}.
\]
Since the two base parameters remain bounded, tails past any fixed \(K\) vanish uniformly as \(K\to\infty\). Orthogonality, the preceding negligible nonisolated bounds, and the full-set product coefficient \(b_{n,t}^{n}\to0\) now give
\[
 \|f_{n,t}-g_{n,t}\|_{L^2(\pi_n)}\longrightarrow0.
\]
The same argument gives
\[
 \chi^2(P^0_{n,t}\|\pi_n)
 =\sum_{S\ne\varnothing}\lambda_n(S)^{2t}
 \longrightarrow\sum_{k\ge1}\frac{a_c^{2k}}{k!}
 =e^{a_c^2}-1.
\]

**5. Gaussian profile.** Under \(\pi_n\), the variables \(\epsilon_i=\chi_{\{i\}}(Y)\) are independent fair signs. Therefore
\[
 \log g_{n,t}(Y)
 =\frac n2\log(1-b_{n,t}^2)
  +\operatorname{arctanh}(b_{n,t})\sum_{i=1}^n\epsilon_i
 \ \Longrightarrow\ \mathcal N(-a_c^2/2,a_c^2).
\]
Moreover, \(\mathbb E_{\pi_n}g_{n,t}^2=(1+b_{n,t}^2)^n\to e^{a_c^2}\); this gives uniform integrability of \(g_{n,t}\) and \(|g_{n,t}-1|\). With \(Z\sim\mathcal N(-a_c^2/2,a_c^2)\), direct Gaussian integration yields
\[
 \frac12\mathbb E|e^Z-1|=2\Phi(a_c/2)-1.
\]
Finally, total variation is bounded by one-half the density \(L^1(\pi_n)\) distance, which is at most one-half the \(L^2(\pi_n)\) distance. Therefore the same limiting profile holds for the actual edge-refresh chain. Its endpoints as \(c\to-\infty\) and \(c\to+\infty\) are one and zero, respectively, giving cutoff.

## Verification

The included standalone Python program `verify.py` checks the cyclic-run counting formula against all subsets on cycles of sizes \(3\) through \(8\), independently constructs the exact rational transition distributions at times \(1\) through \(4\), and tests every associated Walsh coefficient against \(\lambda_n(S)^t\). It also compares enumerated and run-grouped chi-square sums and evaluates the \(L^2\) discrepancy for dimensions \(50,100,200,500\). On execution, it printed `VERIFY_OK 2097`. These computations verify finite instances and identities, not the infinite-limit argument, which is given above.

## Relationship to prior work

Collevecchio and Griffiths (2020, arXiv:2002.09059), especially Theorem 3.3, already provide a general spectral representation for a broad class of hypercube chains; the Walsh diagonalization above is a *specialization of an established technique*, not claimed as new. Their explicit block example partitions coordinates into nonoverlapping blocks, and their Theorem 3.13 treats a different, coordinate-exchangeable nonlocal walk, rather than the overlapping nearest-neighbor edge-refresh chain. Neither inspected statement supplies the present asymptotic \(L^2\) product approximation or its Gaussian total-variation profile.

Blanca, Caputo, Sinclair and Vigoda (2017, arXiv:1708.01513) develop general spatial-mixing bounds for block dynamics, and Blanca, Caputo, Chen, Parisi, Štefankovič and Vigoda (2021, arXiv:2103.07459) obtain mixing/entropy bounds for arbitrary heat-bath blocks. These broader frameworks are consistent with rapid mixing but do not determine the particular cutoff location, window profile or approximation for this specific cycle chain. Salez (2021, arXiv:2102.05597) gives structural sufficient conditions for cutoff but does not give this finite-dimensional Fourier limit or Gaussian profile. The fresh result is the explicit asymptotic distributional comparison and profile in the overlapping-edge model, not the existence of a Walsh basis, a stationary product measure, or generic fast mixing.

## Limitations

The asymptotic assertions fix \(c\) before sending \(n\) to infinity; they do not give a uniform rate in \(c\). The limiting independent-bit law is an approximation near the cutoff window, not an exact formula for the finite-step joint distribution. The present proof applies to the unbiased binary cycle with homogeneous edge selection; it does not immediately extend to general graphs, weighted blocks or interacting spin systems. The finite checks do not certify infinite-dimensional asymptotics. Historical priority has not been independently audited: equivalent earlier work may exist under stochastic coordinate refreshing, block Gibbs sampling, or hypercube walks with local support.

## References

1. A. Collevecchio and R. Griffiths, *Three steps mixing for general random walks on the hypercube at criticality* (first public version 2020-02-20), arXiv:2002.09059, https://arxiv.org/abs/2002.09059 .
2. A. Blanca, P. Caputo, A. Sinclair, and E. Vigoda, *Spatial Mixing and Non-local Markov chains* (first public version 2017-08-03), arXiv:1708.01513, https://arxiv.org/abs/1708.01513 .
3. A. Blanca, P. Caputo, Z. Chen, D. Parisi, D. Štefankovič, and E. Vigoda, *On Mixing of Markov Chains: Coupling, Spectral Independence, and Entropy Factorization* (first public version 2021-03-12), arXiv:2103.07459, https://arxiv.org/abs/2103.07459 .
4. J. Salez, *Cutoff for non-negatively curved Markov chains* (first public version 2021-02-10), arXiv:2102.05597, https://arxiv.org/abs/2102.05597 .
