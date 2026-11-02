# Exact 2-adic valuations on a Mersenne stratum of a binomial-parity run-length transform

## Finding
Let \(\operatorname{rem}_2(z)\in\{0,1\}\) be the least nonnegative residue of an integer \(z\) modulo two, and define
\[
T(n)=\sum_{k=0}^{n}\operatorname{rem}_2\!\left(\binom{n+5k}{2k}\binom nk\right),\qquad n\ge0.
\]
Then for every integer \(r\ge1\),
\[
\boxed{\nu_2(T(2^{10r-6}-1))=\nu_2(T(2^{10r-1}-1))=2+\nu_2(r).}
\]
In particular the valuations are unbounded along each of these two naturally specified subsequences. More generally, if every maximal run of ones in the binary expansion of \(n\) has length \(\ell\equiv4\pmod5\), then
\[
\boxed{\nu_2(T(n))=\sum_{\ell\in\mathcal L(n)}\left(2+\nu_2\!\left(\left\lfloor\frac{\ell-4}{10}\right\rfloor+1\right)\right).}
\]
The multiset \(\mathcal L(n)\) retains repeated run lengths. The empty sum for \(n=0\) is zero.

## Assumptions and scope
The binomial coefficients are ordinary integer binomial coefficients, and the bracketed residues in the definition of \(T\) are summed as **integers**, not reduced modulo two after summation. For a positive integer \(a\), \(\nu_2(a)\) is its exponent of two. The theorem concerns all positive \(r\) and all nonnegative \(n\) in the specified binary-run class. It uses the following published identity, not reproved here: Theorem 14 of Rampersad and Wiebe (2023) states that \(T\) is the run-length transform of the integer sequence \(s\) defined by
\[
s_0=1,\quad s_1=s_2=2,\quad s_3=3,\qquad
s_{m+4}=s_{m+3}+s_{m+2}-s_{m+1}+s_m\quad(m\ge0).
\]
Consequently \(T(2^m-1)=s_m\) and \(T(n)=\prod_{\ell\in\mathcal L(n)}s_\ell\), with the empty product equal to one.

## Proof
**Step 1: the invertible companion matrix.** Put
\[
M=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\1&-1&1&1\end{pmatrix},\qquad
v=\begin{pmatrix}1\\2\\2\\3\end{pmatrix},\qquad e=(1,0,0,0).
\]
Then \(s_m=eM^mv\) for \(m\ge0\). Since \(\det M=-1\), the recurrence extends uniquely to all negative integers by the same formula, with integer terms. In particular, the backward recurrence gives \(s_{-6}=s_{-1}=0\).

**Step 2: a tenth-power congruence.** Exact integer matrix multiplication gives
\[
M^{10}=\begin{pmatrix}9&-4&8&12\\12&-3&8&20\\20&-8&17&28\\28&-8&20&45\end{pmatrix}=I+4B,
\]
where \(B\) is an integral matrix. Its first-row actions on the two backward states are
\[
eBM^{-6}v=\frac{s_4-s_{-6}}4=1,\qquad
eBM^{-1}v=\frac{s_9-s_{-1}}4=9,
\]
because direct recurrence gives \(s_4=4\), \(s_9=36\).

**Step 3: exact 2-adic lifting.** For any integral matrix \(B\) and integer \(r\ge1\), the binomial theorem in \(\mathbb Q_2\) gives
\[
\frac{(I+4B)^r-I}{4r}
=B+\sum_{j=2}^{r}\frac{4^{j-1}}j\binom{r-1}{j-1}B^j.
\]
For \(j\ge2\), the coefficient of \(B^j\) lies in \(2\mathbb Z_2\), since \(2(j-1)-\nu_2(j)\ge1\) and the binomial coefficient is an integer. Thus the quotient is an integral 2-adic matrix congruent to \(B\pmod2\). Multiplication by \(e\) and either integral state \(M^{-6}v\) or \(M^{-1}v\) gives odd 2-adic integers. As both corresponding backward terms vanish,
\[
s_{10r-6}=e\bigl(M^{10r}-I\bigr)M^{-6}v=4r\,u_r,
\quad
s_{10r-1}=e\bigl(M^{10r}-I\bigr)M^{-1}v=4r\,w_r,
\]
where \(u_r,w_r\in\mathbb Z_2^\times\) are odd units. The terms on the left are positive integers for \(r\ge1\), so in each case their exact 2-adic valuation is \(2+\nu_2(r)\).

**Step 4: binary runs.** Every length \(\ell\equiv4\pmod5\) has a unique representation \(\ell=10r-6\) or \(\ell=10r-1\), with \(r=\lfloor(\ell-4)/10\rfloor+1\). The preceding calculation determines \(\nu_2(s_\ell)\). The run-length product formula makes the valuations add over the multiset of binary 1-runs, proving the second assertion. For \(n=0\), \(T(0)=s_0=1\), as required.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It recomputes \(M^{10}\), the two negative-index zeros and odd lifting coefficients, evaluates the recurrence through index 1400, tests both valuation progressions for \(1\le r<140\), and independently evaluates the original binomial-parity sum by Lucas' criterion for Mersenne lengths \(0\) through \(9\) and \(14\). These finite checks test arithmetic and transcription; the proof for all \(r\) is Step 3.

## Relationship to prior work
Rampersad and Wiebe (2023), Theorem 14, identify exactly this binomial-parity sum as the run-length transform of the specified fourth-order recurrence. Their Theorem 13 instead has lower binomial index \(2n+2k\) and different initial terms; the shared recurrence coefficients do not transfer the present valuation assertion. Their treatment of average values in Section 6 does not address the 2-adic valuations stated here. Wu (2022) establishes run-length methods for other binomial-parity sums, but not this Theorem-14 recurrence valuation. The new step is the arithmetic zero-shift and 2-adic matrix lifting yielding an exact unbounded valuation profile. Searches found no directly covering result; no claim is made of an exhaustive global priority check.

## Limitations
This work relies on the cited published run-length identity. It establishes the valuation formula for 1-run lengths congruent to four modulo five; it does not determine valuations of every other run length or every integer \(n\). The finite checker is not an independent audit or an infinite proof. An unindexed equivalent argument may exist.

## References
1. Narad Rampersad and Max Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012, first public 2023-09-07, especially Theorem 14 and Section 6. https://arxiv.org/abs/2309.04012
2. Chai Wah Wu, *Sums of products of binomial coefficients mod 2 and run length transforms of sequences*, INTEGERS 22 (2022), article A81, 2022-08-24. https://math.colgate.edu/~integers/w81/w81.pdf
