# Exact two-point residue laws for consecutive central trinomial coefficients modulo eight

## Finding

Let \(T_n=[x^0](x^{-1}+1+x)^n\) for every integer \(n\geq0\), and let \(\mathcal R=\{1,3,5,7\}\). For \(j\in\mathcal R\), define \(\alpha(j)=((j-1)/2)\bmod2\), so \(\alpha(1)=\alpha(5)=0\) and \(\alpha(3)=\alpha(7)=1\). For every \(j,k\in\mathcal R\) and integer \(N\geq1\), define the consecutive-residue count
\[
P_{j,k}(N)=\#\{0\leq n<N:T_n\equiv j\pmod8,\ T_{n+1}\equiv k\pmod8\}.
\]
Then, simultaneously for all sixteen ordered pairs,
\[
\boxed{P_{j,k}(N)=\begin{cases}N/12+O(\sqrt N),&\alpha(j)=\alpha(k),\\N/24+O(\sqrt N),&\alpha(j)\ne\alpha(k).\end{cases}}
\]
The implied constants are absolute. All sixteen limits are positive. Consequently, conditioned on a starting residue \(j\), each target \(k\) has limiting probability \(1/3\) if \(\alpha(j)=\alpha(k)\), and \(1/6\) otherwise. Although each individual odd residue is asymptotically equally frequent, successive residues are not asymptotically independent. The exponent \(1/2\) is optimal for a uniform bound across the entire sixteen-pair family: no replacement by \(O(N^\theta)\) with \(\theta<1/2\) holds for every pair.

## Assumptions and scope

The constant term defines the ordinary integer central trinomial coefficients. All congruences are integer congruences. The digit sum \(s_2(u)\) is the number of ones in the binary expansion of a nonnegative integer \(u\), and \(e_2(u)\) counts overlapping occurrences of the adjacent binary pattern `11`, equivalently \(e_2(u)=\operatorname{popcount}(u\mathbin{\&}(u\!\gg\!1))\). Higher binary digits are zero by convention. The result concerns the natural-density limit of two adjacent terms modulo eight; it makes no claim about higher moduli or general shifts.

## Proof

**1. Known pointwise congruence and its precise role.** A digit formula for \(T_n\pmod8\) is given in Krattenthaler--Müller, Theorem 17 (arXiv:1608.05657), Section 8.4. In equivalent notation, put
\[
a(n)=s_2(\lfloor n/2\rfloor)\bmod2,\qquad b(n)=e_2(n)\bmod2.
\]
The already-known formula is
\[
T_n\equiv1+2a(n)+4b(n)\pmod8.\tag{1}
\]
It is used as an input, not claimed as a new result. Its equivalence to the parity-specific formula in the cited work follows by substituting the binary low digit: \(s_2(\lfloor n/2\rfloor)=s_2(n)-(n\bmod2)\). The four pairs \((a,b)\) correspond bijectively to \(j=1,3,5,7\).

**2. Binary-carry increments.** Fix \(n\geq0\), let \(t=\nu_2(n+1)\), and write uniquely
\[
n=2^{t+1}H+2^t-1\qquad(H\geq0).
\]
The low \(t\) bits of \(n\) are ones and bit \(t\) is zero; passing to \(n+1\) replaces those ones with zeros and replaces bit \(t\) with one. Let \(h=H\bmod2\). Directly counting the parity contributions of the shifted digit sum and the adjacent `11` occurrences gives
\[
(a(n+1)-a(n),\ b(n+1)-b(n))\pmod2=
\begin{cases}(0,h),&t=0,\\(t\bmod2,\ (h+t-1)\bmod2),&t\geq1.\end{cases}\tag{2}
\]
This includes \(H=0\) and all trailing-run boundary cases. For fixed \(t\), the initial two parities are affine translates of \((s_2(H),e_2(H))\pmod2\): both shifts equal \(\max(t-1,0)\bmod2\). Thus the joint pair is determined by three binary statistics of \(H\): \(s_2(H)\bmod2\), \(e_2(H)\bmod2\), and \(H\bmod2\).

**3. Uniform eight-class digit equidistribution.** For each \((u,v,w)\in\{0,1\}^3\), except \((0,0,0)\), define
\[
S_{u,v,w}(M)=\sum_{0\leq H<M}(-1)^{u s_2(H)+v e_2(H)+w(H\bmod2)}.
\]
We claim \(S_{u,v,w}(M)=O(\sqrt M)\), uniformly over the seven nonzero triples and all integers \(M\geq1\). Split \([0,M)\) into at most one aligned interval of length \(2^k\) at each scale \(k\). On any aligned interval, the high binary prefix is fixed and the low \(k\) bits vary freely; contributions of the prefix only change the terminal bit weight and an overall sign. If \(v=1\), appending the variable bits uses, up to harmless transposition and diagonal signs, the transfer matrix
\[
M_u=\begin{pmatrix}1&1\\(-1)^u&-(-1)^u\end{pmatrix},\qquad M_uM_u^{\mathsf T}=2I.
\]
The initial and terminal conditional-weight vectors have bounded Euclidean norm, so the character sum on a block of size \(2^k\) has modulus at most \(C2^{k/2}\). If \(v=0\), then at least one of \(u,w\) is nonzero: its character sum vanishes for each aligned block of length \(2^k\) once \(k\geq2\), because a varying bit above the least significant position supplies a free sign cancellation; the two smaller scales are uniformly bounded. Summing the geometric series in \(2^{k/2}\) proves the claim. Walsh inversion therefore gives, for each \((c,d,h)\in\{0,1\}^3\),
\[
\#\{0\leq H<M:(s_2(H),e_2(H),H)\equiv(c,d,h)\pmod2\}=\frac M8+O(\sqrt M).\tag{3}
\]
In particular \((a(n),b(n),h)\) is asymptotically uniform on each fixed-trailing-run slice, with a uniform error constant independent of \(t\).

**4. Exact limiting pair probabilities and all-cutoff error.** For the slice \(t=\nu_2(n+1)\), the count of eligible values of \(H\) with \(0\leq n<N\) is \(M_t=N/2^{t+1}+O(1)\). Formula (3) implies that each of the eight initial-parity/next-high-bit triples contributes \(M_t/8+O(\sqrt{M_t})\), uniformly over \(t\). The total proportion of indices having \(t=0\) tends to \(1/2\); those with positive odd \(t\) to \(1/3\); and those with positive even \(t\) to \(1/6\). By (2), on the first and third groups \(\Delta a=0\), whereas on the middle group \(\Delta a=1\). On each group, \(\Delta b\) is equally likely to be zero or one because \(h\) is uniform. Therefore, for each fixed initial parity state \((a,b)\), the joint probabilities of its two transitions preserving \(a\) are each \(\frac14(\frac12+\frac16)\frac12=\frac1{12}\). Its two transitions changing \(a\) each have probability \(\frac14\frac13\frac12=\frac1{24}\). Summing the slice errors yields
\[
\sum_{t\leq\log_2(N+1)}O\!\left(\sqrt{N/2^{t+1}}+1\right)=O(\sqrt N),
\]
since the extra logarithmic term is absorbed by \(\sqrt N\). This proves the theorem for all cutoffs, not only dyadic cutoffs. Values with \(t\) exceeding the largest possible index do not arise.

**5. Sharpness.** Put \(B_r=\sum_{0\leq n<2^r}(-1)^{e_2(n)}\). The two-state signed digit transfer for \(e_2\) has matrix \(M_0=\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\) and \(M_0^2=2I\). Starting with the two one-bit weights \((1,1)\), direct multiplication gives \(B_r=2^{\lceil r/2\rceil}\) for every \(r\geq1\). By the known congruence (1), \(B_r\) is the difference between the number of starting coefficients in residues \(\{1,3\}\) and those in \(\{5,7\}\), for \(n<2^r\). These one-point counts are row sums \(\sum_kP_{j,k}(2^r)\), whose proposed sixteen-pair main terms all sum to \(2^r/4\) in each row. Thus if every pair had error \(O(N^\theta)\) for some \(\theta<1/2\), the displayed \(B_r\) would be \(O(2^{r\theta})\), contradicting \(B_r=2^{\lceil r/2\rceil}\). Sharpness is simultaneous, not claimed individually for each ordered pair.

## Verification

The accompanying standard-library script `artifacts/verify.py` checks the known digit congruence against two independent coefficient calculations, the binary-carry transition formula on a long initial interval, the proposed sixteen-pair count scale against complete dyadic enumerations, and the relevant signed transfer identity. It verifies finite cases only; the exact argument above proves the all-index claim.

## Relationship to prior work

Krattenthaler and Müller, Section 8.4, Theorem 17, give the pointwise modulo-eight digit formula (1); that result is explicitly antecedent and is strictly stronger for determining any single coefficient. The present result does not claim (1) as new. What is added is the two-point natural-density **transition matrix**, its nonuniform conditional probabilities despite uniform single-term marginal frequencies, an all-cutoff square-root discrepancy bound for all sixteen transitions, and the sharpness of that exponent. The cited article does not state these assertions in its inspected section. Beukers develops general prime-power linear schemes for combinatorial sequences; such schemes are a broad framework but do not give this explicit consecutive-pair law. Rowland and Yassawi study automatic congruences for rational diagonals and a modulo-four central trinomial model, without the present two-point modulo-eight asymptotics. The published pointwise formula logically permits a separate derivation of the pair law, but that derivation involves a nontrivial carry partition and uniform signed-transfer estimates; originality is claimed only for the new quantitative theorem, subject to the literature risks below.

## Limitations

No conclusion is asserted for nonconsecutive shifts, other moduli, or a sharp error constant for any individual pair. A full exhaustive literature census is impossible; the known pointwise digit classification might have been used in an unindexed source to derive these transition probabilities or a stronger block-correlation theorem. The bound and sharpness are established for the family simultaneously; they do not establish optimality for each individual pair. The proof assumes the published digit congruence as a verified mathematical input, corroborated by independently computed examples, rather than reproving every detail of the source's original argument.

## References

1. C. Krattenthaler and T. W. Müller, *Motzkin numbers and related sequences modulo powers of 2*, arXiv:1608.05657, Section 8.4, Theorem 17 (first preprint 2016-08-19). https://arxiv.org/abs/1608.05657
2. F. Beukers, *p-Linear schemes for sequences modulo p^r*, arXiv:2211.15240 (first preprint 2022-11-28). https://arxiv.org/abs/2211.15240
3. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, Section 4.2. https://arxiv.org/abs/1310.8635
4. T. D. Noe, *On the Divisibility of Generalized Central Trinomial Coefficients*, Journal of Integer Sequences 9 (2006), Article 06.2.7. https://cs.uwaterloo.ca/journals/JIS/VOL9/Noe/noe35.html
