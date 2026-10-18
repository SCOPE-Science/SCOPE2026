# Equal-block coarsening preserves ultra-log-concavity

## Finding
Let \(X\) have a probability mass function \((a_n)_{n\ge0}\) with interval support and be ultra-log-concave (ULC):
\[
 n a_n^2\ge(n+1)a_{n-1}a_{n+1}\qquad(n\ge1).
\]
For **every** integer \(m\ge1\), define \(Y=\lfloor X/m\rfloor\) and
\[
 b_k=\Pr(Y=k)=\sum_{j=0}^{m-1}a_{mk+j}\qquad(k\ge0).
\]
Then \((b_k)\) is ULC:
\[
 k b_k^2\ge(k+1)b_{k-1}b_{k+1}\qquad(k\ge1).
\]
If \(m\ge2\), the inequality is strict whenever \(b_{k-1}b_{k+1}>0\). Consequently, for \(X\sim\operatorname{Poisson}(\mu)\), \(\mu>0\), and \(m\ge2\), \(Y\) is strictly ULC and strictly underdispersed:
\[
 \operatorname{Var}(Y)<\mathbb E[Y].
\]
Equivalently, the number of arrivals by time \(t>0\) in the ordinary renewal process with independent \(\operatorname{Erlang}(m,\lambda)\) interarrival times is strictly ULC and strictly underdispersed for every integer shape \(m\ge2\) and rate \(\lambda>0\).

## Assumptions and scope
A nonnegative sequence has **interval support** when the indices of its positive terms form an interval of integers, possibly finite or a singleton. This rules out internal zeros. We assume the displayed ULC inequalities at all positive integer indices, with the convention that probabilities at negative indices are zero. The coarsening blocks are consecutive and aligned at zero, all of the **same positive integer width** \(m\); no assertion is made for unequal widths or arbitrary partitions.

The Poisson corollary takes \(X\) to be the number of events of a rate-\(\lambda\) Poisson process in time \(t\), so \(\mu=\lambda t\). Grouping successive \(m\) exponential waiting times produces the Erlang renewal process and its number of completed groups is exactly \(\lfloor X/m\rfloor\).

## Proof
**Step 1 (factorial-weighted log-concavity).** Define \(c_n=n!a_n\). The ULC inequality is equivalent to \(c_n^2\ge c_{n-1}c_{n+1}\). For a log-concave nonnegative sequence with interval support, whenever integers \(r\le u,v\le s\) satisfy \(r+s=u+v\), one has \(c_uc_v\ge c_rc_s\): this follows by comparing successive ratios within the positive interval; when the outer product vanishes the conclusion is immediate.

For each \(k\ge1\) and \(0\le j,l<m\), apply this with
\[
 r=m(k-1)+j,\quad s=m(k+1)+l,\quad
 u=mk+j,\quad v=mk+l.
\]
Indeed, both middle indices lie between the outer indices and their sums coincide. Thus
\[
 c_{mk+j}c_{mk+l}\ge
 c_{m(k-1)+j}c_{m(k+1)+l}.
\]

**Step 2 (a sharp factorial-factor comparison).** Set
\[
 A_{k,j}=\frac{k!}{(mk+j)!}\qquad (k\ge0,\ 0\le j<m).
\]
The positive ratios satisfy
\[
 \frac{A_{k,j}}{A_{k-1,j}}
 =\frac{k}{\prod_{v=1}^m[m(k-1)+j+v]},\qquad
 \frac{A_{k+1,l}}{A_{k,l}}
 =\frac{k+1}{\prod_{v=1}^m[mk+l+v]}.
\]
The first ratio decreases as \(j\) increases, and the second ratio decreases as \(l\) increases. Their worst comparison occurs at \(j=m-1\), \(l=0\), where they are **equal**:
\[
 \frac{k}{\prod_{v=0}^{m-1}(mk+v)}
 =\frac{k+1}{\prod_{v=1}^{m}(mk+v)}.
\]
Consequently,
\[
 A_{k,j}A_{k,l}\ge A_{k-1,j}A_{k+1,l},
\]
strictly if \(m\ge2\) and \(j<m-1\) or \(l>0\).

**Step 3 (cross-pair comparison and summation).** Put \(Q_{k,j}=k!a_{mk+j}=A_{k,j}c_{mk+j}\). Multiplying the inequalities from Steps 1 and 2 yields
\[
 Q_{k,j}Q_{k,l}\ge Q_{k-1,j}Q_{k+1,l}
 \qquad(k\ge1,\ 0\le j,l<m).
\]
Summing over all \(m^2\) ordered pairs gives
\[
 (k!b_k)^2\ge[(k-1)!b_{k-1}][(k+1)!b_{k+1}],
\]
which is exactly the asserted ULC inequality. If \(m\ge2\) and \(b_{k-1}b_{k+1}>0\), interval support of \((a_n)\) forces \(a_{mk}>0\). In the \((j,l)=(0,0)\) summand, both left factors are therefore positive, and the factorial comparison is strict, so the summed inequality is strict.

**Step 4 (underdispersion of Erlang counts).** For a Poisson input all block probabilities are positive; hence the coarsened distribution is strictly ULC. Its tails are dominated by Poisson tails, so all moments exist. Define \(R(k)=(k+1)b_{k+1}/b_k\). Strict ULC makes \(R\) strictly decreasing. The elementary identities
\[
 \mathbb E[R(Y)]=\mathbb E[Y],\qquad
 \mathbb E[Y R(Y)]=\mathbb E[Y(Y-1)]
\]
imply
\[
 \operatorname{Var}(Y)-\mathbb E[Y]
 =\operatorname{Cov}(Y,R(Y))<0,
\]
since \(Y\) is nondegenerate and \(R\) is strictly decreasing. The renewal interpretation was established in the scope paragraph.

## Verification
The self-contained `verify.py` uses only the Python standard library, including exact rational arithmetic. Execute it with `python3 verify.py`. It checks the factorial-ratio comparison directly for a grid of integers, checks each cross-pair inequality and the resulting ULC inequalities for exact finite-support log-concave factorial-weighted distributions, and tests strictly positive Poisson-like rational examples. For example, at \(m=2\), \(\mu=1\), the Poisson block probabilities at indices \(0,1,2\) are respectively \(2e^{-1}\), \(2e^{-1}/3\), and \(e^{-1}/20\), so their first ULC difference is exactly \(11e^{-2}/45>0\). These are diagnostics, **not substitutes** for the quantified proof above; no finite enumeration certifies the infinite range of indices or all distributions.

## Relationship to prior work
Puig, Valero and Fernández-Fontelo (first published 7 August 2023) discuss count underdispersion produced by renewal processes. Their Section 2.1 cites an increasing-failure-rate sufficient condition for underdispersion, covering integer-shape Erlang arrivals, but gives no ultra-log-concavity result or preservation result under block coarsening. ULC is stronger than the variance comparison they establish.

Badiella, del Castillo and Puig (available online 26 June 2023) establish preservation of ULC under **discrete order statistics**, using synchronized sequences. An order statistic of independent replicates is not the deterministic block map \(x\mapsto\lfloor x/m\rfloor\) of a single count; their theorem does not imply the present statement. The cross-pair strategy is related to synchronization but uses a separate sharp factorial-factor comparison to handle coarsening. Classical ULC closure under convolution and thinning likewise does not directly identify this deterministic transformation. Searches for grouped Poisson, renewal counting, sequence coarsening, and ULC formulations did not reveal the present complete statement, but failed searches alone cannot establish priority.

## Limitations
No claim is made for non-ULC inputs, non-interval support, unequal or offset block boundaries, random block widths, or general noninteger-shape Gamma renewals. The quantitative size of the strict ULC gap is not classified. The published-literature novelty conclusion is provisional: older results may use different terminology, and some relevant grouped-Poisson papers could only be inspected at abstract level. Independent audit and priority verification have not been performed.

## References
1. P. Puig, J. Valero, A. Fernández-Fontelo, *Some mechanisms leading to underdispersion: Old and new proposals*, Scandinavian Journal of Statistics 51 (2024), 245–267, first published 7 August 2023. DOI: 10.1111/sjos.12677. https://onlinelibrary.wiley.com/doi/10.1111/sjos.12677
2. L. Badiella, J. del Castillo, P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters 201 (2023), 109900, available online 26 June 2023. DOI: 10.1016/j.spl.2023.109900. https://doi.org/10.1016/j.spl.2023.109900
3. O. Johnson, *Log-concavity and the maximum entropy property of the Poisson distribution*, Stochastic Processes and their Applications 117 (2007), 791–802. DOI: 10.1016/j.spa.2006.10.006.
