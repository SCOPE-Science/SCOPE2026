# Exact q-ary image spectrum and Gaussian output-length law for threshold-one contextual deletions

## Finding

Fix an alphabet \(\Sigma\) with \(|\Sigma|=q\ge2\). For a nonempty source \(x\in\Sigma^n\), split \(x\) into maximal constant runs, and delete the first symbol of every run except the initial run, with the deletion sites assessed **on the original input**. Write the resulting deterministic output as \(T(x)\). For any nonempty word \(y\), let \(r(y)\) denote its number of maximal constant runs and \(m=|y|\).

**Theorem (full image and length spectrum).** For every \(n\ge1\),
\[
 y\in T(\Sigma^n)\quad\Longleftrightarrow\quad m+r(y)-1\le n.
\]
In particular, writing \(N_{n,m}\) for the number of **distinct** attainable outputs of length \(m\),
\[
 N_{n,m}=q\sum_{j=0}^{\min(m-1,n-m)}\binom{m-1}{j}(q-1)^j\qquad(1\le m\le n),
\]
with \(N_{n,m}=0\) outside this range. The complete bivariate image enumeration is
\[
 \mathcal{N}_q(z,t)=\sum_{n\ge1}\sum_{m\ge1}N_{n,m}z^n t^m
 =\frac{qtz}{(1-z)(1-tz-(q-1)tz^2)}.
\]
The **exact maximal zero-error code size** for this deterministic channel is \(N_n=\sum_m N_{n,m}\). With \(\lambda_q=(1+\sqrt{4q-3})/2\), its normalized asymptotic capacity is
\[
 \lim_{n\to\infty}\frac{1}{n}\log_q N_n=\log_q\lambda_q.
\]
For \(q=2\), the binary image size simplifies to \(N_n=2(F_{n+2}-1)\), with \(F_0=0,F_1=1\).

Let \(L_n\) be the length of an output selected uniformly from the **distinct** elements of \(T(\Sigma^n)\) (not the channel output induced by a uniform input). Put
\[
 \mu_q=\frac12+\frac{1}{2\sqrt{4q-3}},\qquad
 \sigma_q^2=\frac{q-1}{(4q-3)^{3/2}}>0.
\]
Then \(\mathbb E[L_n]=\mu_q n+O_q(1)\), \(\operatorname{Var}(L_n)=\sigma_q^2n+O_q(1)\), and
\[
 \frac{L_n-\mu_q n}{\sqrt{\sigma_q^2n}}\ \Longrightarrow\ \mathcal N(0,1).
\]

## Assumptions and scope

All words and alphabets are finite; \(q\ge2\), \(n\ge1\). Every maximal run after the first loses exactly one leading symbol, regardless of its length. Deletion positions refer to the *original* runs and are removed simultaneously. In particular, a run of length one after the initial run disappears, and deleting it can merge neighboring surviving runs. Empty received words never occur because the first input symbol always survives. The zero-error statement concerns a deterministic channel at fixed source blocklength, and the output-length law samples uniformly among *distinct* received words; it does not assume uniform source inputs or independent deletion errors.

## Proof

**1. Image criterion.** Suppose \(x\) has \(s\) runs. The channel removes exactly \(s-1\) symbols, so \(|T(x)|=n-s+1=m\). Deletion cannot increase the number of runs; hence \(r(T(x))\le s\), and therefore \(m+r(T(x))-1\le n\).

Conversely, write \(y=a_1^{\ell_1}\cdots a_r^{\ell_r}\), with positive integers \(\ell_i\) and \(a_i\ne a_{i+1}\). Define the source
\[
 x_0=a_1^{\ell_1}a_2^{\ell_2+1}\cdots a_r^{\ell_r+1}.
\]
It has length \(m+r-1\) and is mapped to \(y\): in each noninitial run, precisely the artificially added first symbol is deleted. If \(n>m+r-1\), append exactly \(n-m-r+1\) singleton runs, each using a symbol different from the immediately preceding one. This is possible for every \(q\ge2\). Each added singleton is removed, leaving \(y\). Thus the criterion is both necessary and sufficient for **every** \(n\), including both endpoints \(n=1\) and \(m=n\).

**2. Counting.** A length-\(m\) word with \(r\) runs is specified by \(r-1\) of the \(m-1\) gaps between letters, a first symbol (\(q\) choices), and each subsequent run symbol (\(q-1\) choices), giving \(q\binom{m-1}{r-1}(q-1)^{r-1}\) words. Summing over \(r-1\le n-m\) proves the finite histogram. To count by *least* feasible source length, the first run of \(y\) contributes \(q\,tz/(1-tz)\); every additional run contributes \((q-1)tz^2/(1-tz)\). Summing the geometric series gives \(qtz/(1-tz-(q-1)tz^2)\). Since a word of least feasible length \(h\) occurs as a distinct output at *all* source lengths \(n\ge h\), multiplication by \((1-z)^{-1}\) produces \(\mathcal N_q\).

For \(q=2\), the least-length coefficients of \(2z/(1-z-z^2)\) are \(2F_n\) for \(n\ge1\). Their partial sums equal \(2(F_{n+2}-1)\).

**3. Optimal zero-error coding and capacity.** Each received word has a nonempty preimage. A zero-error code cannot contain two distinct sources with identical outputs, so its size is at most the number \(N_n\) of output fibers. Selecting one representative from each fiber attains \(N_n\), exactly. The denominator \(1-z-(q-1)z^2\) has positive dominant reciprocal root \(\lambda_q\), satisfying \(\lambda_q^2=\lambda_q+q-1\). The coefficient sequence of \(\mathcal N_q(z,1)\) has exponential growth \(\lambda_q^n\) times a positive constant, since \(\lambda_q>1\) and all competing poles have larger modulus. Taking \(\log_q\) proves the capacity.

**4. Gaussian length law.** For \(t\) near \(1\) define
\[
 \lambda_q(t)=\frac{t+\sqrt{t^2+4(q-1)t}}2.
\]
The positive pole \(z=1/\lambda_q(t)\) of \(\mathcal N_q(z,t)\) is simple and uniformly strictly smaller in modulus than the pole at \(z=1\) and the other quadratic pole. Rational coefficient extraction therefore yields, uniformly for complex \(s\) near zero,
\[
 \mathbb E[e^{sL_n}]=\frac{[z^n]\mathcal N_q(z,e^s)}{[z^n]\mathcal N_q(z,1)}
 =A_q(s)\left(\frac{\lambda_q(e^s)}{\lambda_q(1)}\right)^n(1+O_q(\eta^n)),
\]
where \(A_q\) is analytic, nonzero near zero, \(A_q(0)=1\), and \(0<\eta<1\). Differentiating the logarithm at zero yields the stated mean and variance with bounded additive errors:
\[
 \left.\frac{d}{ds}\log\lambda_q(e^s)\right|_{s=0}=\mu_q,
 \qquad \left.\frac{d^2}{ds^2}\log\lambda_q(e^s)\right|_{s=0}=\sigma_q^2.
\]
Because \(\sigma_q^2>0\), substituting \(s=i\theta/\sqrt{\sigma_q^2n}\), subtracting the linear term, and Taylor-expanding the analytic logarithm gives characteristic-function convergence to \(e^{-\theta^2/2}\). This proves the asserted central limit theorem, without inferring an infinite law from finite enumeration.

## Verification

The supplied standalone Python program directly constructs all source words and deletes the run-leading symbols from their **original** positions. For \(q=2,3,4,5\) and respective maximum source lengths \(12,9,7,6\), it confirms equality of the full observed image set with the run criterion and verifies every length-spectrum coefficient. Across \(34\) parameter pairs it examines \(79,087\) source words. The deterministic program prints `VERIFY_OK` after all assertions.

The asymptotic capacity and Gaussian limit are justified by the proof's analytic pole argument and not by the finite program. To reproduce the finite checks, run `python3 verify_contextual_k1.py` with standard Python 3; no nonstandard dependencies are needed.

## Relationship to prior work

Chen, Milenkovic, Ribeiro and Sima, *Correcting Contextual Deletions in DNA Nanopore Readouts*, arXiv:2602.05072 (first public version 2026-02-04), define the contextual deletion after the run preceding the deleted first symbol and study the deterministic extremal regime \(p=1\). Their Section V analyzes nontrivial fixed thresholds with forbidden-pattern capacity bounds. The present finding isolates the natural **threshold-one endpoint**, derives its complete image language and all finite-length spectra over every \(q\)-symbol alphabet, and establishes exact capacity and a Gaussian image-length law. It does not claim the contextual channel model or the use of run decompositions as new.

Con and Ribeiro, *Channels with Input-Correlated Synchronization Errors*, arXiv:2504.14087 (first public version 2025-04-18), develop general capacity-existence/equality methods for input-dependent synchronization errors and study independent deletion within runs. These results do not supply the specific deterministic run-boundary image language or enumeration. Standard run-composition and rational-generating-function techniques are used in the present proof.

## Limitations

The result is only for deterministic threshold \(k=1\), with all eligible deletions applied. It does not determine the fixed-threshold \(k\ge2\) capacities or positive-probability \(0<p<1\) channel capacities. The q-ary extension concerns the stated deterministic rule, not an experimentally calibrated sequencing model. The code-size claim is existential via one representative per output; computationally efficient fixed-rate encoders are not analyzed. The Gaussian law describes uniform distinct outputs, not the induced distribution from random sources. Possible equivalent formulations in older transducer/image-enumeration literature have not been ruled out conclusively.

## References

1. Y.-P. Chen, O. Milenkovic, J. Ribeiro, and J. Sima, *Correcting Contextual Deletions in DNA Nanopore Readouts*, arXiv:2602.05072, initial submission 2026-02-04. https://arxiv.org/abs/2602.05072
2. R. Con and J. Ribeiro, *Channels with Input-Correlated Synchronization Errors*, arXiv:2504.14087, initial submission 2025-04-18. https://arxiv.org/abs/2504.14087
