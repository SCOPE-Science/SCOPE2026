# Exact stabilization of nonnegative binary 11-block changes under two-bit shifts

## Finding

Let \(r(n)\) count the possibly overlapping occurrences of the binary word `11` in the ordinary base-two expansion of an integer \(n\ge0\). For every integer \(a\ge1\), put
\[
D_a(n)=r(n+2^a+1)-r(n),\qquad
\mu_a(j)=\operatorname{dens}\{n\ge0:D_a(n)=j\}.
\]
All the densities \(\mu_a(j)\) exist. Their **complete nonnegative part** is determined by the polynomial
\[
Q_a(z)=\sum_{j\ge0}\mu_a(j)z^j.
\]
For \(a=1,2,3,4,5,6\), respectively,
\[
\begin{aligned}
Q_1(z)&=(8z^2+22z+17)/64,\\
Q_2(z)&=(2z^3+4z^2+7z+9)/32,\\
Q_3(z)&=(16z^3+36z^2+62z+59)/256,\\
Q_4(z)&=(24z^3+92z^2+122z+105)/512,\\
Q_5(z)&=(6z^3+22z^2+33z+26)/128,\\
Q_6(z)&=(24z^3+88z^2+130z+109)/512.
\end{aligned}
\]
For **every \(a\ge7\)** the distribution stabilizes exactly:
\[
\boxed{Q_a(z)=(12z^3+44z^2+65z+54)/256.}
\]
The threshold is sharp because \(Q_6\ne Q_7\). In particular,
\[
\operatorname{dens}\{n\ge0:r(n+2^a+1)\ge r(n)\}=175/256
\qquad(a\ge7).
\]
Moreover \(D_a(n)>3\) has density zero for every \(a\ge1\) (in fact it never occurs).

## Assumptions and scope

The shift is exactly \(t_a=2^a+1\) for integers \(a\ge1\). Runs are not counted: \(r(n)\) counts adjacent pairs of ones, so a run of \(h\) ones contributes \(h-1\) when \(h\ge1\). The conclusion concerns natural densities on the nonnegative integers. No assertion about the negative tail of \(\mu_a\) being independent of \(a\) is made.

## Proof

Write the binary digits of \(n\) and \(n+t_a\), from low to high, as \(x_i\) and \(y_i\), respectively, and let \(c_i\) be the carry into position \(i\). With zero initial preceding digits, the change in adjacent-one count contributed on reading the next digit pair is
\[
\delta_i=y_{i-1}y_i-x_{i-1}x_i.
\]
We use eight states \((u,v,c)\in\{0,1\}^3\), in lexicographic order: \(u\) and \(v\) are the previous input and output digits, and \(c\) is the carry. For a prescribed shift digit \(e\in\{0,1\}\), define the exact rational-function transition matrix \(M_e(z)\) by adding, for each \(x=0,1\), a weight \(z^{vy-ux}/2\) to the transition
\[
(u,v,c)\longrightarrow(x,y,\lfloor(x+e+c)/2\rfloor),\qquad
 y\equiv x+e+c\pmod2.
\]
Thus the matrix entries specify, with no approximations, the probability and the change statistic of each input bit.

After the highest nonzero shift digit, all following shift digits are zero. Let \(H_{uvc}(z)\) denote the exact expected generating function of the remaining change. If \(c=0\), then
\[
H_{uv0}(z)=\begin{cases}1,&u=v,\\ (1+z^{v-u})/2,&u\ne v.\end{cases}
\]
If \(c=1\), a zero input bit stops the carry and a one continues it. The continuing state is \((1,0,1)\), giving
\[
H_{101}(z)=\frac{z(1+z)}{2(2z-1)},\qquad
H_{uv1}(z)=\frac{z^v(1+z)}4+\frac{z^{-u}}2 H_{101}(z).
\]
The geometric carry tail converges as a Laurent expansion about infinity (for \(|z|>1/2\)). Therefore, with \(e_{000}\) the row basis vector of the initial state, the complete change generating function is exactly
\[
F_a(z)=e_{000}M_1(z)M_0(z)^{a-1}M_1(z)H(z).
\]
The polynomial part at infinity of \(F_a\), consisting of its powers \(z^j\) for \(j\ge0\), is precisely \(Q_a\). Exact multiplication yields the six displayed exceptions and
\[
Q_7(z)=(12z^3+44z^2+65z+54)/256.
\]
This finite calculation is independently reproducible in `check_11_block_law.py`.

It remains to prove that the calculation at \(a=7\) extends to every larger \(a\). The zero-shift transition matrix satisfies the explicitly verifiable characteristic identity
\[
\det(\lambda I-M_0(z))=\lambda^6(\lambda-1)(\lambda-(2z)^{-1}).
\]
Cayley--Hamilton therefore gives, for all \(a\ge7\),
\[
F_{a+2}-F_{a+1}=\frac{F_{a+1}-F_a}{2z}.
\]
A second exact finite multiplication, again checked in the bundled verifier, gives
\[
F_8(z)-F_7(z)=-\frac{(z-1)^2(z+1)(4z^5-8z^4+2z^3-4z^2+2z-1)}{2048z^8(2z-1)}.
\]
Its numerator has degree \(8\) and denominator degree \(9\); hence its Laurent series at infinity contains only strictly negative powers. Every subsequent increment is obtained by multiplying this by another power of \((2z)^{-1}\), so every \(F_a\) with \(a\ge7\) has the same nonnegative polynomial part. This proves the stabilization and sharpness.

For completeness, the distribution computed from a random infinite sequence of independent fair binary input digits equals the natural density asserted in the theorem. For a fixed shift, the input and output bits become equal after the carry has ceased and one further bit has been read. Failure to resolve the difference within an additional \(L\) random digits requires an uninterrupted carry across those \(L\) digits, whose probability is at most \(2^{-L}\). Truncating there gives an event depending on finitely many low digits, a union of complete residue classes modulo a power of two, with exactly its dyadic probability as natural density. Letting \(L\) increase establishes existence and identifies the density with the matrix-generated probability. If a finite integer \(n\) had \(D_a(n)>3\), choosing a long enough finite high-zero termination would produce a positive-measure cylinder of infinite digit strings with the same change. Because the proven generating function has no nonnegative powers above degree \(3\), this is impossible; thus the stronger pointwise assertion also holds.

## Verification

Run `python3 check_11_block_law.py` with Python 3 and SymPy. The verifier constructs the eight-state matrices from the bit-addition rule; computes twelve exact rational generating functions and their polynomial parts; checks the matrix characteristic identity and its Cayley--Hamilton consequence; proves the rational increment has no nonnegative powers; and directly enumerates binary blocks for the seven small shift parameters. It finishes with `VERIFY_OK`. The exact polynomial and matrix identities, not the finite enumeration, certify the infinite statement.

## Relationship to prior work

Sobolewski and Spiegelhofer [1] introduced the adjacent-`11` change distributions, established their existence, and gave conditional distribution recurrences (Proposition 3.2) and asymptotic Gaussian estimates for shifts having many one-blocks. Those recurrences can in principle compute individual finite shifts. The theorem here gives an explicit **uniform sharp stabilization threshold**, including the complete nonnegative mass function, for the natural two-set-bit family whose number of one-blocks remains bounded. The broader block-counting generalization [2] treats Gaussian approximation for many one-blocks, not the stated sparse-shift exact law. The binary-digit-sum analogue [3] concerns a different statistic. OEIS A014081 [4] tabulates \(r(n)\) itself, not this family of change distributions.

## Limitations

The full negative-change distributions still depend on the separation parameter. No extension to arbitrary shifts, other patterns, or positive-density subsets of all shifts is asserted. The literature comparison gives best-known distinctness from inspected material, not an absolute priority or independent validation certificate.

## References

[1] B. Sobolewski and L. Spiegelhofer, *Block occurrences in the binary expansion*, arXiv:2309.00142, first posted 2023-08-31, https://arxiv.org/html/2309.00142 .

[2] B. Sobolewski, *On the behavior of binary block-counting functions under addition*, arXiv:2412.15851, first posted 2024-12-20, https://arxiv.org/abs/2412.15851 .

[3] M. Drmota, M. Kauers and L. Spiegelhofer, *On a Conjecture of Cusick Concerning the Sum of Digits of n and n+t*, arXiv:1509.08623, 2015, https://arxiv.org/abs/1509.08623 .

[4] OEIS A014081, *Number of occurrences of '11' in the binary expansion*, https://oeis.org/A014081 .
