# Sharp leading constant for period-doubling periodic complexity
## Finding
Let \(\mathbf{pd}\) be the period-doubling word, the fixed point beginning in \(0\) of
\[
0\mapsto01,\qquad 1\mapsto00.
\]
Let \(p(n)\) be its local period at position \(n\), let
\[
P(n)=\sum_{0\le j<n}p(j),
\]
and let \(h(n)=P(n)/n\) be its periodic complexity.

Then
\[
h(n)=\frac23\log_2 n+O(\log\log n),
\]
or equivalently
\[
P(n)=\frac23 n\log_2 n+O(n\log\log n).
\]
In particular,
\[
\lim_{n\to\infty}\frac{h(n)}{\log_2 n}=\frac23.
\]

A quantitative scale identity underlying the result is
\[
\left|P(2n)-2P(n)-\frac43n\right|
\le \frac53\bigl(\lfloor\log_2 n\rfloor+1\bigr)
\qquad(n\ge1).
\]

## Assumptions and scope
The local period is the one used by Mignosi--Restivo and Rampersad: \(p(i)\) is the least positive length of a prefix of the suffix beginning at \(i\) that is comparable by the suffix relation with the prefix ending at \(i-1\). The period-doubling word is recurrent, so every local period is finite.

The proof starts from Rampersad's published six-dimensional linear representation of \(p(n)\). No unproved statement about the growth of a generic regular sequence is used. The theorem identifies the first-order asymptotic constant; it does not claim a bounded second-order fluctuation.

## Proof
Use the published representation
\[
p(n)=vM_{\varepsilon_{r-1}}\cdots M_{\varepsilon_0}w,
\]
where \(\varepsilon_{r-1}\cdots\varepsilon_0\) is the binary expansion of \(n\),
\[
v=(1,0,0,0,0,0),\qquad w=(1,1,1,1,1,1)^T,
\]
and
\[
M_0=
\begin{pmatrix}
1&0&0&0&0&0\\
0&0&0&1&0&1\\
0&0&0&0&0&2\\
0&0&0&0&1&0\\
0&0&0&1&0&1\\
0&0&0&0&0&0
\end{pmatrix},
\quad
M_1=
\begin{pmatrix}
0&1&1&0&0&0\\
0&0&0&0&1&0\\
0&0&0&0&0&0\\
0&1&1&0&0&0\\
0&1&1&0&0&0\\
0&0&2&0&0&0
\end{pmatrix}.
\]
Write \(r(n)=vM_{\varepsilon_{r-1}}\cdots M_{\varepsilon_0}\), so \(r(2n)=r(n)M_0\) and \(r(2n+1)=r(n)M_1\).

Define
\[
q(n)=p(2n)+p(2n+1)-2p(n)-1.
\]
Direct multiplication of the displayed matrices gives a seven-state \(2\)-kernel. With states numbered \(0,\ldots,6\), their outputs and transitions on the least-significant bit are
\[
\begin{array}{c|c|cc}
\text{state}&\text{output}&0&1\\ \hline
0&0&1&2\\
1&0&3&4\\
2&0&4&5\\
3&0&1&6\\
4&0&4&4\\
5&1&6&2\\
6&1&6&6
\end{array}.
\]
Thus \(q(n)\in\{0,1\}\). Let \(a\) and \(b\) be the sequences represented by states \(1\) and \(2\). The table gives
\[
q(2n)=a(n),\qquad q(2n+1)=b(n),
\]
\[
a(0)=0,\quad a(2n+1)=0,\quad a(2n)=1-a(n)\ \ (n\ge1),
\]
and
\[
b(0)=0,\quad b(2n)=0,\quad b(2n+1)=1-b(n).
\]

Put
\[
A(n)=\sum_{j<n}a(j),\qquad B(n)=\sum_{j<n}b(j),\qquad Q(n)=\sum_{j<n}q(j).
\]
For \(n\ge1\), the preceding recurrences imply
\[
A(2n)=n-1-A(n),
\]
\[
A(2n+1)=n-A(n)-a(n),
\]
\[
B(2n)=B(2n+1)=n-B(n).
\]
If
\[
e_A(n)=3A(n)-n,\qquad e_B(n)=3B(n)-n,
\]
then
\[
e_A(2n)=-e_A(n)-3,
\]
\[
e_A(2n+1)=-e_A(n)-1-3a(n),
\]
\[
e_B(2n)=-e_B(n),
\]
and
\[
e_B(2n+1)=-e_B(n)-1.
\]
Induction on binary length therefore gives
\[
|e_A(n)|\le4L(n),\qquad |e_B(n)|\le L(n),
\]
where \(L(n)=\lfloor\log_2n\rfloor+1\) for \(n\ge1\).

Since
\[
Q(2n)=A(n)+B(n)
\]
and
\[
Q(2n+1)=A(n)+B(n)+a(n),
\]
we obtain
\[
|3Q(n)-n|\le5L(n).
\]
On the other hand,
\[
P(2n)-2P(n)
=\sum_{j<n}\bigl(p(2j)+p(2j+1)-2p(j)\bigr)
=n+Q(n).
\]
Consequently
\[
\left|P(2n)-2P(n)-\frac43n\right|
\le\frac53L(n).
\]

Writing \(H(n)=P(n)/n\), this becomes
\[
H(2n)=H(n)+\frac23+O\left(\frac{\log n}{n}\right).
\]
Iterating at a fixed positive integer \(m\) gives, uniformly in \(k\ge0\),
\[
H(2^km)=H(m)+\frac23k+O\left(\frac{\log(m+1)}{m}\right).
\]
Indeed, the accumulated error is dominated by
\[
\frac{5}{6m}\sum_{j\ge0}\frac{L(m)+j}{2^j}
=O\left(\frac{\log(m+1)}m\right).
\]

To pass from dyadic rays to all integers, let \(s=\lceil\log_2 n\rceil\), and choose \(k\) so that
\[
s2^k\le n<2s2^k.
\]
Set \(m=\lfloor n/2^k\rfloor\), so \(s\le m<2s\) and
\[
2^km\le n<2^k(m+1).
\]
Rampersad's published bounds give \(H(m)=O(\log m)\). Hence the dyadic-ray estimate at the two endpoints yields
\[
H(2^km)=\frac23\log_2 n+O(\log m)
\]
and the same estimate with \(m+1\). Since \(P\) is increasing and the two endpoints differ from \(n\) by a relative factor \(1+O(1/m)\), dividing by \(n\) changes these endpoint estimates by only \(O(\log n/m)=O(1)\). Finally \(m\asymp\log n\), so
\[
H(n)=\frac23\log_2 n+O(\log\log n).
\]
This proves the finding.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier first generates the period-doubling word and checks the local-period definition directly at the first \(128\) positions against the published matrix representation. It reproduces the published initial row
\[
1,2,4,1,1,8,2,2,2,2,16,1,1,4,4,1.
\]

It then verifies the seven affine kernel states and every transition exactly by integer matrix multiplication. The induced recurrences for \(q,a,b\) are replayed for the first \(20000\) indices.

Finally it checks the discrepancy bound and exact doubling identity through \(n=50000\), and independently reproduces the published closed formula for \(P(2^\ell)\) through \(\ell=15\). These finite checks validate the matrix algebra and implementation; the asymptotic statement follows from the proof above.

## Relationship to prior work
Rampersad's primary paper gives the same six-dimensional representation of the period-doubling local-period sequence. It explicitly notes that the general regular-sequence asymptotic theorem is inconclusive here because the joint-spectral-radius bound reaches the dominant eigenvalue. The paper then proves only
\[
\frac13\log_2 n-\frac1{18}
\le h(n)\le
\frac43\log_2 n+3
\]
and an exact formula on the dyadic subsequence.

The present argument uses the same representation but applies it to the scale increment \(p(2n)+p(2n+1)-2p(n)\). That increment collapses to a binary automatic sequence with logarithmic summatory discrepancy, which determines the missing global leading constant.

Focused searches under the exact periodic-complexity terminology, the constant \(2/3\), the doubling identity, local-period aliases, and later period-doubling work located the primary paper but no published theorem implying the displayed global asymptotic.

## Limitations
The theorem determines the leading constant and gives an \(O(\log\log n)\) error for the averaged complexity. It does not identify a bounded second-order fluctuation, and it does not claim that the \(O(\log\log n)\) term is sharp.

The proof depends on the published linear representation for the period-doubling local-period sequence. The verifier checks this representation directly from the local-period definition only on a finite prefix; the representation itself is treated as a published premise for the infinite theorem.

## References
1. N. Rampersad, “The periodic complexity function of the Thue–Morse word, the Rudin–Shapiro word, and the period-doubling word,” arXiv:2112.04416v1, first public 2021-12-08; Australasian Journal of Combinatorics 85(2) (2023), 150–158.
2. P. Dumas, “Joint spectral radius, dilation equations, and asymptotic behavior of radix-rational sequences,” Linear Algebra and its Applications 438 (2013), 2107–2126.
3. C. Heuberger and D. Krenn, “Asymptotic analysis of regular sequences,” Algorithmica 82 (2020), 429–508, arXiv:1810.13178.
