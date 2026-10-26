# Root-length spectrum and odd-start density of \(2\)-binomial squares in the Thue–Morse word

## Finding
Let \(t=t_0t_1\cdots\) be the one-sided Thue–Morse word, with \(t_j=s_2(j)\bmod 2\) for \(j\ge0\), where \(s_2\) counts binary ones. A \(2\)-binomial square at position \(i\) with root length \(m\ge1\) is a factor \(uv=t_i\cdots t_{i+2m-1}\) with \(|u|=|v|=m\) such that every binary scattered subsequence of length at most two has equal multiplicity in \(u\) and \(v\).

**Theorem.** The set of possible root lengths is exactly
\[
\{m\ge1:\exists i\ge0\text{ with a }2\text{-binomial square of root }m\}
=2\mathbb Z_{\ge1}\cup\{1,3\}.
\]
Moreover, for the only nontrivial odd root length \(m=3\), the starting positions are *exactly* \(i=2a+1\), where \(a\ge0\) and \(t_at_{a+1}t_{a+2}t_{a+3}\) is `0011` or `1100`. These positions have natural density \(1/12\) among all nonnegative starting positions. Every \(2\)-binomial square with odd root length in \(t\) is an ordinary literal square.

For every even root length \(m=2h\), explicit witnesses are as follows. If \(h\) is even, one can take \(i=0\). If \(h\) is odd, choose any integer \(k\) satisfying \(2^k>h\) and \(k\equiv s_2(h-1)\pmod2\), put \(b=2^k-h\), and take \(i=4b+2\). In either case the two root blocks have equal \(2\)-binomial signatures.

## Assumptions and scope
All positions are zero-based in the infinite one-sided word; factors are contiguous, but the subsequences counted in the equivalence are scattered. This is \(2\)-**binomial**, not \(2\)-abelian equivalence. The spectrum is existential in the starting position; the odd-root density counts all starting positions, including those where more than one root length works. No circular wrapping is used. The root length is strictly positive.

## Proof
**Binary moment criterion.** If \(w=w_0\cdots w_{m-1}\) has \(K(w)=\sum_jw_j\) ones and first moment \(M(w)=\sum_jjw_j\), its number of scattered `01` subsequences is \(M(w)-\binom{K(w)}2\). All other length-at-most-two scattered counts are determined by \(m\), \(K(w)\), and this count. Thus for equal-length binary words \(u,v\),
\[
u\sim_2v\iff K(u)=K(v)\text{ and }M(u)=M(v).
\]
This proves the needed normalization of the binomial signature, including constant words and lengths one and two.

**Odd-root rigidity.** Write \(m=2h+1\) with \(h\ge0\). The substitution relations \(t_{2j}=t_j\) and \(t_{2j+1}=1-t_j\) show that each aligned pair \((t_{2j},t_{2j+1})\) contains exactly one one. If a length-\(2m\) candidate begins at even \(i\), it contains exactly \(m\) ones, an odd number. The two halves cannot then have equal one-counts.

Hence \(i=2a+1\). Put \(S_1=\sum_{r=1}^h t_{a+r}\), \(S_2=\sum_{r=h+1}^{2h}t_{a+r}\). The first half consists of one odd-position letter followed by \(h\) aligned complementary pairs; the second consists of \(h\) aligned pairs followed by one even-position letter. Their respective counts and local first moments are
\[
\begin{aligned}
K(u)&=h+1-t_a, &M(u)&=h(h+1)-S_1,\\
K(v)&=h+t_{a+2h+1}, &M(v)&=h^2-S_2+2h\,t_{a+2h+1}.
\end{aligned}
\]
The equal-count condition gives \(t_{a+2h+1}=1-t_a\). Substituting this into the equal-moment condition gives
\[
S_2-S_1=h(1-2t_a).
\]
Since \(0\le S_1,S_2\le h\), equality is possible precisely when the source word \(t_a\cdots t_{a+2h+1}\) is \(0^{h+1}1^{h+1}\) or \(1^{h+1}0^{h+1}\). The Thue–Morse word has no factor `000` or `111`: every three consecutive letters contain an aligned complementary pair. Thus \(h+1\le2\), or \(m\in\{1,3\}\). The criterion gives the asserted exact source patterns for \(m=3\). At \(m=1\), `11` at position \(1\) is a witness; at \(m=3\), `101101` at position \(11\) is a witness. Both are literal squares. No other odd roots occur.

**Every even root occurs.** Set \(m=2h\) and start at \(i=2a\). The two length-\(2h\) halves are the Thue–Morse substitution images of \(t_a\cdots t_{a+h-1}\) and \(t_{a+h}\cdots t_{a+2h-1}\). Each image has \(h\) ones. In local coordinates its moment is \(h^2\) minus the number of ones in its length-\(h\) preimage, because the unique one in each image pair lies at coordinate \(2r+1-t_{a+r}\). The halves are therefore \(2\)-binomially equivalent exactly when their preimages are *abelianly* equivalent.

For even \(h\), taking \(a=0\) works: each adjacent length-\(h\) source block begins at an even index and consists of \(h/2\) complementary pairs. For odd \(h=2r+1\), take \(a=2b+1\). The two length-\(h\) source blocks have respective one-counts \(r+1-t_b\) and \(r+t_{b+h}\), so they match iff \(t_b\ne t_{b+h}\). With the stated \(k\) and \(b=2^k-h\), the complement identity
\[
s_2(2^k-h)=k-s_2(h-1)
\]
gives \(t_b=0\) and \(t_{b+h}=t_{2^k}=1\). Thus the proposed index \(i=2a=4b+2\) works for every odd \(h\). This proves all even roots occur, without extrapolating computations.

**Exact natural density for root three.** Standard existence of factor frequencies for primitive uniform substitutions applies to \(0\mapsto01,1\mapsto10\). Write \(f_{xy}\) for the limiting frequency of the adjacent pair `xy`. Splitting pair starts by parity yields \(f_{01}=1/4+f_{11}/2\) and \(f_{11}=f_{01}/2\); complementation gives \(f_{10}=f_{01}=1/3\) and \(f_{00}=f_{11}=1/6\). Splitting length-three starts similarly, `010` or `101` arises from source `00` or `11`, so each has frequency \(1/6\). The source length-four factors `0011` and `1100` can start only at odd positions, arising respectively from source triples `101` and `010`; each therefore has frequency \(1/12\). An original root-three starting position must be odd, \(i=2a+1\), with one of those two source length-four factors at \(a\). Its density is consequently \(\tfrac12(\tfrac1{12}+\tfrac1{12})=\boxed{1/12}\).

## Verification
Run `python3 verify.py` in a Python 3 interpreter with no external packages. It independently generates the first \(32768\) letters by binary digit parity and substitution, tests every binary word of length at most eight against two implementations of the \(2\)-binomial signature, checks the constructive witnesses for every even root up to \(512\), finds no odd root from \(5\) through \(259\) in that prefix, and tests the precise odd-root location criteria at \(6000\) source positions each. These are bounded corroborations; the argument above proves the infinite claims.

## Relationship to prior work
Rigo and Salimov introduced \(k\)-binomial equivalence and discussed the avoidance of \(2\)-binomial squares, while studying the Thue–Morse *equivalence-class complexity*. Rao, Rigo and Salimov established ternary avoidance of \(2\)-binomial squares; their binary Thue–Morse example concerns a \(2\)-binomial cube. Fici, Mignosi and Shallit counted **abelian** squares in Thue–Morse, which is a weaker equivalence. Lejeune, Leroy and Rigo determined \(k\)-binomial factor-class complexity, not the spectrum of neighboring equivalent blocks. These results motivate but do not state the present length-spectrum theorem or odd-root occurrence density. The main new distinction is between what equivalence classes *occur* and which class can appear in two consecutive equal-length positions.

## Limitations
The result does not enumerate the number of even-root occurrences at each length, nor all starting positions for even roots. The density assertion concerns only root length three. Mathematical originality is assessed against searched accessible literature and records, not an exhaustive historical priority certificate.

## References
1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words* (2013), full author preprint, https://orbi.uliege.be/bitstream/2268/149313/2/binomial_final_long.pdf . Publicly archived by 2013-05-27.
2. M. Rao, M. Rigo and P. Salimov, *Avoiding 2-binomial squares and cubes* (2015), author preprint, https://orbi.uliege.be/bitstream/2268/178702/1/final.pdf .
3. G. Fici, F. Mignosi and J. Shallit, *Abelian-Square-Rich Words* (2017), https://arxiv.org/abs/1701.00948 .
4. M. Lejeune, J. Leroy and M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word* (2018 preprint; journal 2020), https://orbi.uliege.be/bitstream/2268/234006/1/binomial-TM-lastVersion.pdf .
