# Exact functional information for q-ary symmetric channels

## Finding

Let \(\mathcal X\) and \(\mathcal Y\) be finite alphabets. Suppose that for each output \(y\), the channel transition law has two levels \(a_y\ge b_y\ge0\). Let \(S_y=\{x:W(y\mid x)=a_y\}\) be the high-likelihood set and \(m_y=P_X(S_y)\). Then
\[
I_F(X\to Y)=\sum_{y:P_Y(y)>0}(a_y-b_y)\bigl[-m_y\log_2m_y\bigr],
\]
where outputs of zero probability are omitted and \(0\log_2 0=0\).

For the q-ary symmetric channel \(W_\epsilon(y\mid x)=1-\epsilon\) if \(y=x\), and \(\epsilon/(q-1)\) otherwise, put \(p_i=P_X(i)\), \(a=1-\epsilon\), \(b=\epsilon/(q-1)\), and \(h_*(u)=-u\log_2u\) with \(h_*(0)=0\). For every \(q\ge2\) and \(\epsilon\in[0,1]\),
\[
I_F(X\to Y)=\begin{cases}
(a-b)H(P_X),&a\ge b,\\
(b-a)\displaystyle\sum_{i=1}^q h_*(1-p_i),&b>a.
\end{cases}
\]
The uniform input maximizes \(I_F\) whenever \(a\ne b\); if \(a=b\), then \(I_F=0\) for every input law.

In the conventional noise range \(0\le\epsilon\le(q-1)/q\), the maximum over input laws of the one-shot lower-bound improvement over mutual information is exactly
\[
\max_{P_X}\bigl(I_F(X\to Y)-I(X;Y)\bigr)
=h_2(\epsilon)+\epsilon\log_2(q-1)-\frac{q\epsilon}{q-1}\log_2q.
\]
For \(0<\epsilon<(q-1)/q\), equality holds only for the uniform input. At \(\epsilon=0\) and \(\epsilon=(q-1)/q\), the gap is zero for every input law.

## Assumptions and scope

All alphabets are finite. The likelihood ratio is interpreted on the support of \(P_X\). The input distribution may have zero-probability symbols; expressions use \(0\log_2 0=0\), and outputs with \(P_Y(y)=0\) are omitted. Functional information is \(I_F(X\to Y)=\mathbb E_Y[D_{CS}(P_{X\mid Y}\|P_X)]\), where \(D_{CS}\) is the differential entropy of the width function \(w_y(\ell)=P_X\{x:P_{X\mid Y}(x\mid y)/P_X(x)\ge\ell\}\). The gap formula is restricted to \(\epsilon\le(q-1)/q\); no worst-case gap formula is claimed for \(\epsilon>(q-1)/q\).

## Proof

For a fixed output \(y\) with \(s_y=P_Y(y)>0\), the posterior-to-prior likelihood ratio on the support of \(P_X\) is \(r_y(x)=W(y\mid x)/s_y\). If \(W(y\mid x)\) takes the high value \(a_y\) on \(S_y\) and the low value \(b_y\) off that set, write \(m_y=P_X(S_y)\). The width function equals \(1\) for \(0\le\ell\le b_y/s_y\), equals \(m_y\) for \(b_y/s_y<\ell\le a_y/s_y\), and equals \(0\) above \(a_y/s_y\). Therefore
\[
D_{CS}(P_{X\mid Y=y}\|P_X)
=-\int_0^\infty w_y(\ell)\log_2w_y(\ell)\,d\ell
=\frac{a_y-b_y}{s_y}\bigl[-m_y\log_2m_y\bigr].
\]
Multiplying by \(s_y\) and summing over outputs proves the two-level formula. If the two levels coincide, the middle interval has zero length and the contribution is zero.

For the q-ary symmetric channel, the high-likelihood set is \(\{y\}\) when \(a>b\), so \(m_y=p_y\) and the sum is \((a-b)H(P_X)\). When \(b>a\), the high-likelihood set is the complement of \(\{y\}\), so \(m_y=1-p_y\) and the second branch follows. The uniform maximizer follows from strict concavity of Shannon entropy in the first branch and strict concavity of \(u\mapsto-(1-u)\log_2(1-u)\) in the second branch. At \(a=b\), all likelihood ratios are one and functional information is zero.

Now assume \(a\ge b\) and write \(c=a-b=1-q\epsilon/(q-1)\). Let \(u\) be the uniform distribution. The output law is \(P_Y=cP_X+(1-c)u\), and the row entropy of the channel is \(H(W(\cdot\mid x))=h_2(\epsilon)+\epsilon\log_2(q-1)\), independent of \(x\). Hence
\[
I_F-I=cH(P_X)-H(P_Y)+h_2(\epsilon)+\epsilon\log_2(q-1).
\]
By concavity of entropy, \(H(P_Y)\ge cH(P_X)+(1-c)\log_2q\). Substitution gives the stated upper bound. The uniform law has \(P_Y=u\), so equality is attained there. Strict concavity gives uniqueness for \(0<c<1\); the endpoint channels have zero gap for every prior. This proves the claim.

## Verification

The proof evaluates the exact width function; finite enumeration is not used as a substitute for the general argument. Boundary checks are explicit: the formula gives \(I_F=H(P_X)\) at \(\epsilon=0\), zero at \(\epsilon=(q-1)/q\), and the complement-entropy branch at \(\epsilon=1\). For \(q=2\), the two branches reduce to \(I_F=|1-2\epsilon|H(P_X)\). The maximum-gap expression is nonnegative and vanishes at the two endpoint regimes by entropy concavity. No independent validation or independent audit is claimed.

## Relationship to prior work

The channel-simulation-divergence literature defines the width-function integral and establishes its role as a lower bound on one-shot relative-entropy coding cost. The 2026 ring-toss-code paper proves an achievability bound within \(\log_2 e\) bits of functional information for bounded likelihood ratios and discusses singular-channel and asymptotic cases. The 2025 non-singular-channel paper proves the general one-shot lower bound and the asymptotic half-logarithmic redundancy. The 2024 causal-rejection-sampling paper introduces the divergence and records the point-mass self-information identity. The inspected texts do not state the two-level finite-channel formula or the exact worst-case gap above for the q-ary symmetric channel. The present result is an explicit structural evaluation of the existing invariant, not a new coding algorithm or asymptotic theorem.

## Limitations

The two-level formula does not give a comparable closed form for channels with three or more distinct transition-probability levels. The exact gap maximization is proved only for \(\epsilon\le(q-1)/q\). The operational rate interval from the cited coding theorem requires its bounded-likelihood-ratio hypothesis; the formula for \(I_F\) itself does not. The result is a narrow exact characterization, and its derivation is direct from the published definition; no independent audit has been performed.

## References

1. S. Hill, F. Alajaji, T. Linder, and G. Flamich, *Rejection Sampling is Optimal for Relative Entropy Coding*, arXiv:2604.23076 (2026).
2. G. Flamich, S. M. Sriramu, and A. B. Wagner, *The Redundancy of Non-Singular Channel Simulation*, arXiv:2501.14053 (2025).
3. D. Goc and G. Flamich, *On Channel Simulation with Causal Rejection Samplers*, arXiv:2401.16579 (2024).
4. G. Flamich, *Data Compression with Relative Entropy Coding*, arXiv:2506.16309 (2025).
