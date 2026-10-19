# An even-shift renewal factor hidden in the fully chaotic logistic map

## Finding
Let \(F(x)=4x(1-x)\) on \([0,1]\), start \(X_0\) from its invariant arcsine probability \(dx/[\pi\sqrt{x(1-x)}]\), and observe \(Z_n=\mathbf 1_{\{X_n>1/4\}}\). The threshold \(1/4\) is the nonfixed preimage of the nonzero fixed point \(3/4\), since \(F(1/4)=F(3/4)=3/4\).

The complete stationary binary law is the output law of the three-state Markov chain with states \(A,B,C\), stationary distribution \((1/3,1/3,1/3)\), transition matrix
\[
P=\begin{pmatrix}
1/2&1/2&0\\
0&0&1\\
1/2&1/2&0
\end{pmatrix},\qquad
Z(A)=0,\quad Z(B)=Z(C)=1.
\]
Its symbolic support is precisely the **even shift**: a finite word is permitted if and only if it contains no subword \(0\,1^{2j+1}\,0\) for any integer \(j\ge0\). Thus its topological entropy is \(\log((1+\sqrt5)/2)\), strictly less than the full logistic-map entropy \(\log2\).

Successive occurrences of zero form a renewal process. Conditional on a zero at time zero, the first positive return time \(R\) obeys
\[
\Pr(R=2j+1\mid Z_0=0)=2^{-(j+1)},\qquad j=0,1,2,\ldots.
\]
Successive such return times are independent and identically distributed. In particular, \(\mathbb ER=3\), and the binary process has entropy rate \(h(Z)=(2/3)\log2\).

For every integer \(n\ge1\),
\[
\Pr(Z_0=\cdots=Z_{n-1}=1)=
\begin{cases}
(2/3)2^{-k},&n=2k+1,\ k\ge0,\\
2^{-k},&n=2k,\ k\ge1.
\end{cases}
\]
Hence the conditional probability of one further \(1\) after a run of \(n\) ones is \(3/4\) when \(n\) is odd and \(2/3\) when \(n\) is even. The binary observation process is therefore not Markov of any finite order.

The full empirical-frequency scaled cumulant generating function exists for every \(t\in\mathbb R\):
\[
\Lambda(t)=\lim_{N\to\infty}\frac1N\log\mathbb E\exp\!\left(t\sum_{n=0}^{N-1}Z_n\right)
=\log\left(\frac{1+\sqrt{1+8e^{2t}}}{4}\right).
\]
The empirical frequency satisfies a large-deviation principle with speed \(N\) and good rate function
\[
I(p)=\frac p2\log\frac{p(2-p)}{8(1-p)^2}-\log\frac{2-p}{4(1-p)},\quad 0<p<1,
\]
continuously extended by \(I(0)=\log2\), \(I(1)=\tfrac12\log2\), and equal to \(+\infty\) outside \([0,1]\). It has its unique zero at \(p=2/3\).

The two-time covariance, already covered by a more general threshold-correlation formula in previous work, is included here only as a consistency check:
\[
\operatorname{Cov}(Z_0,Z_n)=\frac{(-1)^{n+1}}{9\,2^n}\quad(n\ge1),\qquad \operatorname{Var}(Z_0)=\frac29.
\]
Accordingly \(N^{-1/2}\sum_{n=0}^{N-1}(Z_n-2/3)\) converges in distribution to a centered normal with variance \(8/27\), in agreement with \(\Lambda''(0)\).

## Assumptions and scope
The map, measure, and observable are exactly as defined above. All probabilistic statements refer to the stationary process under arcsine initial probability. Threshold-boundary orbits have zero measure; the symbolic support is the closure of the positive-probability finite-word language. The theorem does not assert a topological conjugacy between the logistic interval and the even shift, nor does it cover other sensor thresholds or nonstationary initial laws.

## Proof
**1. Expanding-coordinate representation.** For \(u\) uniform on \([0,1)\), set \(x=\sin^2(\pi u)\). Then \(F(x)=\sin^2(2\pi u)\), so the dynamics are a factor of the doubling map \(D(u)=2u\bmod1\). The pushforward of uniform \(du\) is the normalized arcsine probability. Because \(\sin^2(\pi u)>1/4\) exactly when \(1/6<u<5/6\), the sensor is the indicator of this interval in the doubling coordinate.

**2. Exact Markov partition and lumping.** Partition the circle at the six points \(j/6\) and call its consecutive arcs \(C_j\), \(0\le j\le5\). From \(C_j\), doubling visits each of \(C_{2j\bmod6}\) and \(C_{(2j+1)\bmod6}\) with conditional probability \(1/2\). This is a genuine Markov partition: the map is affine with constant slope \(2\) on every relevant branch and carries each atom onto precisely two atoms. Uniform initial measure therefore gives the stationary six-state Markov law with uniform weights \(1/6\).

Group \(C_0,C_5\) as \(A\), \(C_1,C_4\) as \(B\), and \(C_2,C_3\) as \(C\). Both states in each group have exactly the same total probabilities into each destination group. The lumped chain has the displayed transition matrix, uniform stationary distribution, and emissions \(0,1,1\). Consequently it reproduces every finite observation word probability, not merely the first two moments.

**3. Even shift and returns.** A zero records state \(A\). After departure \(A\to B\), the next state must be \(C\); every subsequent pair \(B\to C\) contributes two ones, and a return to \(A\) can occur only from \(C\). Conversely, every finite word with even-length runs of ones between zeros is a path in this graph. A right-resolving two-vertex presentation of that language has adjacency matrix \(\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\), with Perron root \((1+\sqrt5)/2\). Each visit to \(A\) either immediately returns with probability \(1/2\), or makes an excursion \(A\to B\to C\), after which \(C\to A\) has probability \(1/2\) and \(C\to B\) probability \(1/2\). Thus \(R=2j+1\) has probability \(2^{-(j+1)}\). Independence of successive gaps follows from the strong Markov property at returns to \(A\).

**4. Entropy and infinite memory.** The chain is irreducible and aperiodic because \(A\) has a self-loop. Thus zeros occur infinitely often in both directions in its stationary extension. The most recent zero and the parity of the subsequent run of ones recover the hidden state almost surely, so the symbol factor has the same entropy rate as the hidden chain. Only rows \(A\) and \(C\) are random, each with entropy \(\log2\) and stationary mass \(1/3\). Hence \(h(Z)=(2/3)\log2\). Multiplying the \(B,C\) submatrix or using the displayed transition rules gives the exact all-one probabilities. Their consecutive ratios alternate forever between \(3/4\) and \(2/3\). In a Markov process of finite order \(r\), these ratios would be constant for all \(n\ge r\), a contradiction.

**5. Frequency pressure, deviations, and covariance.** Let \(D_t=\operatorname{diag}(1,e^t,e^t)\). The positive Perron eigenvalue of \(D_tP\) is
\[
\lambda(t)=\frac{1+\sqrt{1+8e^{2t}}}{4},
\]
because its characteristic polynomial is \(z(z^2-z/2-e^{2t}/2)\). Standard finite-state Perron theory shows the moment generating function has exponential growth \(\lambda(t)^N\). The differentiable limiting logarithm gives the large-deviation principle for empirical frequencies; the boundary rates also follow directly from the exact all-zero and all-one cylinder probabilities. Solving \(p=\Lambda'(t)=1-(1+8e^{2t})^{-1/2}\) gives the stated Legendre transform and endpoints.

For the covariance, direct multiplication of the same three-state matrix gives \(C_0=2/9\), \(C_1=1/18\), and \(C_n=(-1/2)C_{n-1}\) for \(n\ge2\). Thus \(C_n=(-1)^{n+1}/(9\,2^n)\) for positive lags. The finite-state Markov central limit theorem applies; the summable covariance series gives variance \(C_0+2\sum_{n\ge1}C_n=8/27\), also equal to \(\Lambda''(0)\).

## Verification
The included standalone script `verify.py` independently enumerates every word through length eleven by exact midpoint sampling in the full six-cell doubling-map refinement; it then compares all \(4094\) word probabilities against the lumped three-state formula, using rational arithmetic. It additionally checks the long all-one and all-zero cylinders, fourteen exact covariance identities, and the characteristic-polynomial coefficients of the exponentially tilted transition matrices at four rational weights. Execution returned `VERIFY_OK 4094 exact word comparisons; 14 covariance checks; 4 tilted-kernel checks`. These finite tests are consistency checks; the above proofs establish the all-length and asymptotic statements.

## Relationship to prior work
Karamanos, Mistakidis, and Mistakidis (arXiv:1608.05876v1, first submitted 2016-08-20) analyze symbol correlations at the **Feigenbaum parameter** using the generating partition at \(x=1/2\). The present stationary \(r=4\) calculation uses instead the nongenerating \(x=1/4\) partition and proves an even-shift factor with a complete renewal law and frequency pressure, so neither setting implies the other as stated.

The stochastic **Even Process** and its infinite Markov order are longstanding examples; its two-state probability-parameter family is explicitly described by Travers and Crutchfield (2014), and the probability-half variant is discussed in the 2017 *Spectral simplicity of apparent complexity II* treatment. Its abstract structural properties are therefore prior art: the contribution claimed here is the identification of this precise process with a physically defined, fixed-point-preimage threshold observation of the fully chaotic logistic map, and the resulting explicit observable-dependent frequency pressure and deviation profile. The known full-parameter Chebyshev binary-threshold covariance formula encompasses the positive-lag covariance displayed above after the conjugate coordinate \(y=1-2x\); that covariance is **not** claimed as original. General Markov coarse-graining and sofic-entropy methods (MacKernan–Nicolis 1994; Froyland–Junge–Ochs 2001) furnish broad computational frameworks; the generic matrix method and even-shift properties themselves are not claimed as original.

## Limitations
The conclusion is confined to the stationary parameter-four logistic map and the distinguished strict threshold \(1/4\). The explicit covariance is independently subsumed by existing general threshold work. Potential earlier specialized realizations of the even shift via this exact logistic sensor remain a historical-priority risk: certain general coarse-graining papers were available only as metadata/abstracts, not full text. No independence from earlier mathematics is claimed, and external independent audit has not been performed.

## References
- K. Karamanos, I. S. Mistakidis, and S. I. Mistakidis, *Symbol-to-symbol correlation function at the Feigenbaum point of the logistic map*, arXiv:1608.05876v1 (first public posting 2016-08-20), https://arxiv.org/abs/1608.05876.
- C. S. Hsu and M. C. Kim, *Construction of maps with generating partitions for entropy evaluation*, Phys. Rev. A **31** (1985), 3253, doi:10.1103/PhysRevA.31.3253.
- D. MacKernan and G. Nicolis, *Generalized Markov coarse graining and spectral decompositions of chaotic piecewise linear maps*, Phys. Rev. E **50** (1994), 988–999, doi:10.1103/PhysRevE.50.988.
- G. Froyland, O. Junge, and G. Ochs, *Rigorous computation of topological entropy with respect to a finite partition*, Physica D **154** (2001), 68–84, doi:10.1016/S0167-2789(01)00216-0.
- *Spectral simplicity of apparent complexity. II. Exact complexities and complexity spectra*, *Chaos* (2017), doi:10.1063/1.4986248 (the classical Even Process and its infinite Markov order).
- N. F. Travers and J. P. Crutchfield, *Infinite Excess Entropy Processes with Countable-State Generators*, *Entropy* **16** (2014), 1396–1413, doi:10.3390/e16031396 (Figure 1, classical Even Process).
