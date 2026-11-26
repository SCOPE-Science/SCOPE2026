# Exact carry formula and unbounded Abelian complexity for radix-\(k\) period doubling

## Finding

Fix an integer \(k\ge3\) and let \(u\) be the one-sided fixed point starting with \(0\) of \(\varphi_k(0)=0^{k-1}1\), \(\varphi_k(1)=0^k\). The substitution is primitive, and its factors generate an aperiodic minimal subshift. For every \(n\ge1\), the number \(\rho_k(n)\) of distinct ones-counts of length-\(n\) factors is given by the two-state signed-carry optimization below, using \(O(\log_k(n+1))\) integer operations. In particular, for all \(m\ge1\),
\[
\rho_k\left(\frac{k^{2m}-1}{k+1}\right)=m+1.
\]
This establishes unbounded Abelian complexity with an exact logarithmic ladder. The separate calculation at lengths that are powers of \(k\) is also implied by known cyclic-class inflation for the same family and is not part of the distinct finding.

## Signed-carry formula

Write \(S(N)=\sum_{j=0}^{N-1}u_j\), and write \(n=\sum_{j=0}^{h-1}a_j k^j\) with leading digit \(a_{h-1}\ne0\). Set \(a_j=0\) for \(j\ge h\). Consider finite-support binary carry sequences \((c_j)_{j\ge0}\) starting at \(c_0=0\), with transitions
\[
c_{j+1}=0\ \text{allowed if }a_j+c_j<k;\qquad
c_{j+1}=1\ \text{allowed if }a_j+c_j>0.
\]
A transition contributes \((-1)^j c_{j+1}\). Let \(L_k(n)\) and \(H_k(n)\) be the minimum and maximum total weights, respectively. Compute both by keeping the minimum and maximum at each of the two possible incoming carries per digit. After the first \(h\) digits, if \(c_h=0\), the tail contributes zero; if \(c_h=1\), the already-counted weight of \(c_h\) can be supplemented by either \(0\) or \((-1)^h\). Then
\[
\rho_k(n)=1+H_k(n)-L_k(n).
\]

## Proof

The substitution gives \(u_{kr+k-1}=1-u_r\), with zero at all other residues. Thus \(u_j\) is the parity of the largest exponent \(v\) for which \(k^v\) divides \(j+1\). Counting multiples of \(k^r\) for \(r\ge1\) gives
\[
S(N)=\sum_{r\ge1}(-1)^{r+1}\left\lfloor N/k^r\right\rfloor,\qquad
(k+1)S(N)-N=\sum_{j\ge0}(-1)^{j+1}d_j(N),
\]
where \(d_j(N)\) are the radix-\(k\) digits, starting at the least significant. The second identity follows by expanding the floor sums and collecting digit coefficients. In adding \(n\) to a start \(M\ge0\), the digit difference at position \(j\) is \(a_j+c_j-kc_{j+1}\). Substitution into the alternating-digit formula yields
\[
S(M+n)-S(M)=S(n)+\sum_{j\ge1}(-1)^{j+1}c_j.
\]
The transition inequalities above are necessary and sufficient: the input digit \(0\) realizes an allowed zero outgoing carry, and \(k-1\) realizes an allowed one. Choices in different columns are independent once the carries are fixed, and a path of finite support is realized by using zero digits above its end. In the all-zero high digits the carry can only continue as a string of ones and then stop, giving the alternating tail corrections shown above; both can be realized. Hence the dynamic program describes the exact extrema. Sliding a window to the right by one changes its ones-count by at most one, so every integer between two attained extrema also occurs. This proves the formula. The number of digits processed is \(h\); a constant number of integer operations is used per digit, including when extracting the digits by repeated division. This is an integer-operation bound, not a bit-complexity claim.

For \(n_m=(k^{2m}-1)/(k+1)\), the least-significant-first digits are \(k-1,0,k-1,0,\ldots,k-1\), of length \(2m-1\). Positive carry contributions are at odd indices; whenever there is a negative contribution at an even index, the immediately preceding odd-index carry had to be one because the odd-index digit is zero. Thus the total weight is nonnegative. Through index \(h=2m-1\) it is at most \(m\), and the additional tail is nonpositive. Weight zero occurs at \(M=0\); weight \(m\) occurs at \(M=\sum_{r=0}^{m-1} k^{2r}\), with a carry out of each \(k-1\) digit that immediately stops at the next zero digit. This proves the asserted ladder.

The second iterate of the substitution sends both letters to words containing both letters, so the fixed point is uniformly recurrent and generates a minimal shift. The alternating-digit formula implies frequency \(1/(k+1)\) since its right-hand side is \(O(\log N)\) for fixed \(k\). The discrepancy from this frequency is unbounded: choose integers with digit \(k-1\) at arbitrarily many even positions and zero at odd ones. An eventually periodic word would instead have bounded discrepancy from its own frequency. This excludes periodicity of the fixed point and of the minimal shift it generates.

## Verification and scope

The supplied finite verifier compares literal substitution prefixes, valuation parity, the prefix formula, and window-count extrema with the carry computation; the reported range includes radices \(3\) through \(6\), with radix two as a comparison. Finite checks are not used to extrapolate the theorem. The statement concerns only the specified binary length-\(k\) substitution and ordinary Abelian complexity. No result for the radix-two case or a general \(k\)-automatic family is proposed as new.

## Related results

- *Cyclic-class inflation for sparse-marker Toeplitz fixed points*, [Resultary theorem and proof](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-cyclic-class-inflation-for-sparse-marker-toeplitz-fixed-points--96c4f2479d45/RESULT.md), gives a substitution bijection of cyclic factor classes at lengths \(n\) and \(kn\) for the same family and transports ones-counts by \(t\mapsto n-t\). Iteration from the two length-one factors gives exactly the floor and ceiling of \(k^m/(k+1)\) at lengths \(k^m\). That result treats this scaling and does not provide the signed-carry optimization at arbitrary lengths or the exact ladder above.
- A. Parreau, M. Rigo, E. Rowland and É. Vandomme, [arXiv:1405.3532](https://arxiv.org/abs/1405.3532), study ordinary and higher Abelian complexity for radix-two examples including period doubling. V. Berthé, P. Cecchi-Bernales and B. Espinoza, [arXiv:2602.04833](https://arxiv.org/abs/2602.04833), Theorem 6.2, give a criterion for global letter balance in primitive aperiodic substitutions. K. E. Bognini and H. Ammar, [arXiv:2511.20881](https://arxiv.org/abs/2511.20881), study a different generalization on a \(k\)-letter alphabet. Historical priority for equivalent high-radix calculations is not settled by these comparisons.
