# Complete consecutive-residue law for Motzkin numbers modulo five

## Finding

For every integer \(n\ge 0\), define the Motzkin number

\[
M_n=\sum_{h=0}^{\lfloor n/2\rfloor}\binom n{2h}C_h,
\qquad C_h=\frac{1}{h+1}\binom{2h}{h}.
\]

For \(j,k\in\{0,1,2,3,4\}\) and \(N\ge1\), let

\[
P_{j,k}(N)=\#\{0\le n<N : M_n\equiv j\pmod 5,\ M_{n+1}\equiv k\pmod 5\}.
\]

**Theorem.** For every ordered residue pair \((j,k)\) and every \(N\ge1\),

\[
P_{j,k}(N)=c_{j,k}N+O\bigl((1+\log_5(N+2))^2\bigr),
\]

where the complete, rational density matrix is

\[
(c_{j,k})_{0\le j,k\le4}=
\frac1{80}\begin{pmatrix}
0&2&2&2&2\\
2&6&6&2&2\\
2&2&6&2&6\\
2&6&2&6&2\\
2&2&2&6&6
\end{pmatrix}.
\]

The implied constant can be taken uniform over all 25 entries. In addition to this asymptotic statement, \(P_{0,0}(N)=0\) **exactly** for all \(N\): no two consecutive Motzkin numbers are both multiples of five. The limiting marginal distribution is \((1/10,9/40,9/40,9/40,9/40)\), but neighboring residues are not asymptotically independent; for example, the limiting frequencies of \((1,1)\) and \((1,3)\) are respectively \(3/40\) and \(1/40\).

## Assumptions and scope

All residues and divisions in this proof are in the finite field \(\mathbb F_5\); denominators \(2\) and nonzero central trinomial residues are invertible. The sequence index begins at zero and the pair at index \(n\) means the ordered values at \(n\) and \(n+1\). The estimate applies to every integer cutoff \(N\), not only powers of five. No unproved analytic assumptions are used.

## Proof

**1. A published digit formula and a consecutive-index identity.** Set \(T_n=[x^0](x^{-1}+1+x)^n\), with \(T_0,T_1,T_2,T_3,T_4\equiv (1,1,3,2,4)\pmod5\). Write \(w=(1,1,3,2,4)\). The central-trinomial Lucas congruence (Deutsch--Sagan; restated by Rampersad--Shallit and Kohen) states that if \(n=\sum_i d_i5^i\), then

\[
T_n\equiv\prod_iw_{d_i}\pmod5.
\]

Thus every \(T_n\) is nonzero modulo five. The exact identity

\[
2M_n=3T_n+2T_{n+1}-T_{n+2}
\]

is classical and is also stated explicitly by Kohen. These two published facts are the only external mathematical inputs.

**2. An explicit finite push-forward rule.** For each \(q\ge0\) put \(U(q)=T_q\pmod5\) and \(R(q)=T_{q+1}/T_q\pmod5\). Both lie in \(\mathbb F_5^\times=\{1,2,3,4\}\). Every \(n\ge0\) is uniquely \(n=5q+d\) with \(0\le d<5\). For \(0\le i\le3\), define the four factors

\[
a_i(d,r)=\begin{cases}w_{d+i},&d+i<5,\\r\,w_{d+i-5},&5\le d+i\le7.\end{cases}
\]

The Lucas congruence gives \(T_{5q+d+i}\equiv U(q)a_i(d,R(q))\pmod5\). Since \(2^{-1}=3\) in \(\mathbb F_5\), write

\[
f_d(r)=3(3a_0+2a_1-a_2),\quad
g_d(r)=3(3a_1+2a_2-a_3)\pmod5.
\]

Then the **exact**, all-index ordered-pair identity is

\[
(M_{5q+d},M_{5q+d+1})\equiv
U(q)(f_d(R(q)),g_d(R(q)))\pmod5.
\]

For \(r=1,2,3,4\) in that order, the complete \((f_d(r),g_d(r))\) table is:

| \(d\) | \(r=1\) | \(r=2\) | \(r=3\) | \(r=4\) |
|---:|:---:|:---:|:---:|:---:|
| 0 | (1,1) | (1,1) | (1,1) | (1,1) |
| 1 | (1,2) | (1,2) | (1,2) | (1,2) |
| 2 | (2,4) | (2,1) | (2,3) | (2,0) |
| 3 | (4,4) | (1,2) | (3,0) | (0,3) |
| 4 | (4,1) | (2,2) | (0,3) | (3,4) |

No cell in this table is \((0,0)\); since \(U(q)\ne0\), the exact nonoccurrence of consecutive zeros follows immediately.

**3. Quantitative joint equidistribution of the multiplier and carry ratio.** For arbitrary \(a,r\ge0\), consider the aligned base-five interval \(I_{a,r}=\{a5^r,\ldots,(a+1)5^r-1\}\). Uniformly in \(a\), \(r\), and \((u,v)\in(\mathbb F_5^\times)^2\), we prove

\[
\#\{q\in I_{a,r}:U(q)=u,R(q)=v\}
=\frac{5^r}{16}+O(r+1). \tag{1}
\]

Let \(h\) be the number of trailing base-five digits equal to \(4\) in the lower \(r\) digits of \(q\). If \(0\le h<r\), the digit just above that run is \(e\in\{0,1,2,3\}\). On adding one, the higher digits are unchanged and

\[
R(q)=4^h\,\frac{w_{e+1}}{w_e}
\quad\text{in }\mathbb F_5^\times. \tag{2}
\]

Since \(4^2=1\), the formula also equals \(4^{-h}w_{e+1}/w_e\). The four ratios for \(e=0,1,2,3\) are \((1,3,4,2)\), a permutation of \(\mathbb F_5^\times\). Thus, for fixed \(v\) and \(h\), exactly one \(e\) is admissible. With that \(e\), the \(r-h-1\) lower free digits contribute a product of independent weights \((1,1,3,2,4)\); factors from \(h,e,a\) are fixed nonzero units.

Let \(A_s(z)\) count length-\(s\) digit words having weight product \(z\in\mathbb F_5^\times\). An exact induction in the four-element multiplicative group gives

\[
A_s(1)=\frac{5^s+3}{4},\qquad
A_s(z)=\frac{5^s-1}{4}\quad(z\ne1). \tag{3}
\]

Indeed at length zero only the empty word has product one; appending a digit multiplies the total convolution by \(5\) and leaves one extra copy at the identity because the digit-weight multiset contains each unit once plus one extra \(1\). Hence for each fixed \(u,v,h<r\), the corresponding number is \(5^{r-h-1}/4+O(1)\). Summing over the \(r\) possible values of \(h\),

\[
\sum_{h=0}^{r-1}\frac{5^{r-h-1}}4
=\frac{5^r-1}{16}.
\]

The unique lower word consisting of \(r\) digits all equal to \(4\) contributes at most one further index (including a possible carry into the prefix \(a\)). This proves (1), including \(r=0\) after absorbing a constant.

**4. Exact limiting matrix and arbitrary cutoffs.** Let \(C_{j,k}\) count triples \((d,u,v)\in\{0,1,2,3,4\}\times(\mathbb F_5^\times)^2\) such that \((uf_d(v),ug_d(v))=(j,k)\). Enumerating the **exactly eighty** triples using the 20-cell table above gives

\[
(C_{j,k})_{0\le j,k\le4}=
\begin{pmatrix}
0&2&2&2&2\\
2&6&6&2&2\\
2&2&6&2&6\\
2&6&2&6&2\\
2&2&2&6&6
\end{pmatrix}.\tag{4}
\]

From (1), any aligned block of \(5^r\) consecutive \(q\)'s contributes exactly \(5^r C_{j,k}/16+O(r+1)\) to the number of qualifying pairs over its five corresponding \(n\)'s per \(q\). Each initial interval \(0\le q<Q\) is a disjoint union of at most four aligned base-five blocks of any given length \(5^r\); the total error is \(O(\sum_{r\le\log_5(Q+1)}(r+1))=O((1+\log_5(Q+1))^2)\). The first \(N=5Q+s\) indices have \(Q\) full groups of five, with \(0\le s<5\) leftover indices. Their \(O(1)\) contribution changes no estimate. Since \(5Q C_{j,k}/80\) is the predicted full-block count and \(N-5Q<5\), (4) gives the claimed density matrix and discrepancy bound for all \(N\).

## Verification

The accompanying standalone Python checker `verify_pairs.py` (only the standard library is needed) derives all twenty \((f_d,g_d)\) pairs, constructs the eighty-triple matrix, verifies the direct integer Motzkin sum and central-trinomial identities for small indices, tests the digit formula, and checks complete dyadic-analogue base-five prefix distributions. Run `python3 verify_pairs.py`; success prints `VERIFY_OK`. This finite check is a safeguard, **not** a substitute for the all-index proof in Sections 1–4.

## Relationship to prior work

Deutsch and Sagan establish central-trinomial congruence machinery and analyze zero positions of Motzkin numbers modulo five. Burns obtains the zero-residue density \(1/10\), already known before this theorem. Rampersad and Shallit establish modular automaticity and uniform recurrence as well as Lucas-type central-trinomial structure. Kohen supplies the adjacent central-trinomial identity and a general recurrence framework. Those results alone do not **state** the entire nonuniform twenty-five-cell pair-frequency matrix or the all-cutoff polylogarithmic discrepancy bound. The new proof explicitly supplies the carry-ratio equidistribution lemma and all twenty push-forward cases. Existing complete automata in the literature could in principle be used to derive pair statistics algorithmically; priority against any unlocated earlier specialization cannot be guaranteed.

## Limitations

The theorem is specific to the standard Motzkin sequence, adjacent indices, and reduction modulo five. It gives a uniform \(O((\log N)^2)\) estimate but does not claim that its logarithmic order is optimal. It does not classify longer blocks, other primes, or lifts modulo higher powers of five. Finite computations do not certify the infinite claims; the proof relies on the cited Lucas congruence and exact adjacent-identity antecedents. A previously unindexed explicit transition theorem would affect priority.

## References

1. Emeric Deutsch and Bruce E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326 (first posted 2004-07-19), Journal of Number Theory 117 (2006), 191–215; https://arxiv.org/abs/math/0407326.
2. Rob Burns, *Structure and asymptotics for Motzkin numbers modulo small primes using automata*, arXiv:1612.08146 (first posted 2016-12-24); https://arxiv.org/abs/1612.08146.
3. Narad Rampersad and Jeffrey Shallit, *Congruence properties of combinatorial sequences via Walnut and the Rowland–Yassawi–Zeilberger automaton*, arXiv:2110.06244 (first posted 2021-10-12); https://arxiv.org/abs/2110.06244.
4. Nadav Kohen, *Uniform recurrence in the Motzkin numbers and related sequences mod p*, arXiv:2403.00149 (first posted 2024-02-29); https://arxiv.org/abs/2403.00149.
5. Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, preprint, 2024; later published in *Integers* (2026); https://nkohen.github.io/publication/2026-01-19-density-and-symmetry-in-the-generalized-motzkin-numbers-modulo-p.
6. OEIS A001006 (Motzkin numbers) and A338220 (indices of zero residues modulo five): https://oeis.org/A001006 and https://oeis.org/A338220.
