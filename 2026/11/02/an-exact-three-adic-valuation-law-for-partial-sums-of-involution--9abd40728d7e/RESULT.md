# An exact three-adic valuation law for partial sums of involution numbers

## Finding

Let \(I_0=I_1=1\) and \(I_n=I_{n-1}+(n-1)I_{n-2}\) for \(n\ge2\), so \(I_n\) is the number of involutions of \(n\) labelled objects. Put \(a_n=\sum_{j=0}^{n}I_j\). The following gives **every three-adic valuation** of the partial sums, with no exceptional indices:
\[
\boxed{\nu_3(a_n)=
\begin{cases}
2,&n\equiv4\pmod9,\\
1,&n\equiv6\pmod9,\\
\nu_3(n+1),&n\equiv8\pmod9,\\
0,&n\not\equiv4,6,8\pmod9.
\end{cases}}
\qquad(n\ge0).
\]
In particular \(3^k\mid a_n\) for \(k\ge3\) **if and only if** \(n\equiv-1\pmod{3^k}\). The valuations are unbounded on the unique compatible branch \(n\equiv-1\), while two additional branches end at precisely valuations one and two. This fully describes the natural three-adic statistic noted, but not correctly classified, in the original study of these partial sums.

## Assumptions and scope

The valuation \(\nu_3\) is taken on positive integers and \(n\) ranges over all nonnegative integers. The coefficient sequence and its partial sums are those of Amdeberhan--Moll, not arbitrary weighted involution counts. No claim is made about primes other than three.

## Proof

**1. An exact binomial identity.** As in the original combinatorial definition of the partial sums, for each positive integer \(N\),
\[
a_{N-1}=\sum_{k\ge0}(2k-1)!!\binom{N}{2k+1},\qquad (-1)!!=1,\tag{1}
\]
where all but finitely many terms vanish. Dividing by \(N\) gives the rational identity
\[
\frac{a_{N-1}}N=\sum_{k\ge0}\frac{(2k-1)!!}{2k+1}\binom{N-1}{2k}.\tag{2}
\]

**2. The unit quotient on multiples of twenty-seven.** We prove
\[
\boxed{\frac{a_{N-1}}{N}\equiv1\pmod3}\qquad\text{for every positive integer }27\mid N,\tag{3}
\]
where (3) asserts that this rational number is a three-adic integer and a unit. Set \(c_k=(2k-1)!!/(2k+1)\). Direct integer valuation gives \(\nu_3(c_0)=0\), \(c_0=1\), \(c_1=1/3\), \(c_4=35/3\), while \(\nu_3(c_k)\ge1\) for all \(k\ge2\) other than \(k=4\). To justify the last infinite assertion without extrapolation, it holds by direct factor count for \(2\le k\le12\), \(k\ne4\). For every \(k\ge13\), the odd double factorial contains at least \(\lfloor(k+1)/3\rfloor\) multiples of three, and
\[
3^{\lfloor(k+1)/3\rfloor-1}\ge2k+1,\tag{4}
\]
so its three-adic valuation is at least one greater than that of \(2k+1\). Inequality (4) holds for \(k=13,14,15\) and persists when \(k\) is increased by three, because its left side triples and its right side increases by six.

For \(27\mid N\), the product representation
\[
\binom{N-1}{m}=(-1)^m\prod_{j=1}^{m}\left(1-\frac Nj\right)
\]
shows for \(m=2,8\) that \(\binom{N-1}{m}\equiv1\pmod9\): each \(j\le8\) has \(\nu_3(j)\le1\). Consequently the only potentially nonintegral summands of (2) combine to
\[
\frac{1}{3}\left[\binom{N-1}{2}+35\binom{N-1}{8}\right]
\equiv\frac{1+35}{3}=12\equiv0\pmod3.
\]
All other summands except the initial \(1\) are multiples of three in \(\mathbb Z_{(3)}\). This proves (3), hence
\[
\nu_3(a_{N-1})=\nu_3(N)\quad\text{whenever }27\mid N.\tag{5}
\]
Here \(\mathbb Z_{(3)}\) denotes rationals with denominator prime to three.

**3. Periods modulo small powers of three.** The established involution congruence
\[
I_{n+3^r}\equiv I_n\pmod{3^r}\qquad(r\ge1,n\ge0)\tag{6}
\]
is also obtained directly from the involution binomial sum by Vandermonde and valuation estimates; it is acknowledged prior work. For any \(r\ge1\), summing (6) over a block yields
\[
a_{n+3^r}-a_n\equiv a_{3^r-1}\pmod{3^r}.\tag{7}
\]
The exact base value \(a_8=1116\) is divisible by nine. For \(r\ge3\), (5) with \(N=3^r\) proves \(3^r\mid a_{3^r-1}\). Therefore \(a_n\) has period dividing \(3^r\) modulo \(3^r\) for every \(r\ge2\). Modulo three, (6) shows that a block of three involution numbers sums to \(1+1+2=4\equiv1\pmod3\); three such blocks yield period nine for \(a_n\bmod3\).

**4. Exhausting the low residue classes.** The recurrence generates the following complete vector of partial sums modulo \(27\), indexed from \(n=0\) to \(n=26\):
\[
(1,2,4,8,18,17,12,1,9,10,2,4,26,18,26,3,19,18,19,2,4,17,18,8,21,10,0).\tag{8}
\]
Together with periods nine modulo three and modulo nine, and period twenty-seven modulo twenty-seven, (8) proves: valuation zero unless \(n\equiv4,6,8\pmod9\); valuation exactly one on \(n\equiv6\pmod9\); valuation exactly two on \(n\equiv4\pmod9\); valuation exactly two on \(n\equiv8,17\pmod{27}\); and valuation at least three only on \(n\equiv26\pmod{27}\). On the last class, (5) applies to \(N=n+1\) and gives valuation exactly \(\nu_3(n+1)\). On the two remaining \(n\equiv8\pmod9\) classes, \(\nu_3(n+1)=2\) already. These exhaustive cases establish the stated formula.

## Verification

Run `python3 verify.py` using Python 3 with only its standard library. The executable independently generates the involution and partial-sum residues by recurrence, checks the exact full 27-entry certificate, tests the valuation formula through 40,000 indices with precision \(3^8\) (truncating any valuation at eight), confirms the binomial identity on an initial exact-integer range, and checks the finite coefficient inequalities and special cancellations used in the proof. Finite tests corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work

The first public version of Amdeberhan--Moll's *Involutions and their progenies* was submitted 9 June 2014. Its Theorem 5.1 identifies the partial sums and Note 6.4 suggests an odd-prime valuation pattern for them; for the prime three its printed conditions do not match even the values \(a_4=18\) and \(a_8=1116\). The theorem above supplies a correct, exact formula for every index and explains the three distinct positive-valuation branches. We do **not** claim the involution recurrence, the partial-sum identity, or modular periodicity as new. Miska--Ulas (2019 preprint, 2020 journal) develops far-reaching general results for permutation sequences and discusses partial sums; its inspected statements do not give this explicit formula for \(\nu_3(a_n)\). Related work may include an equivalent unlocated specialization.

## Limitations

The result is specific to three-adic valuations of these partial sums. Its complete proof uses a three-adic unit calculation special to the first odd factorial denominators. It does not extend automatically to other primes or to other permutation-counting families. Literature searches cannot establish absolute priority, and independent mathematical audit has not been performed.

## References

1. T. Amdeberhan and V. H. Moll, *Involutions and their progenies*, arXiv:1406.2356 (first submitted 9 June 2014), *Journal of Combinatorics* **6** (2015), 483–508; see Theorem 5.1 and Note 6.4. https://arxiv.org/abs/1406.2356
2. P. Miska and M. Ulas, *On some properties of the number of permutations being products of pairwise disjoint d-cycles*, arXiv:1904.03395 (2019), *Monatshefte für Mathematik* **192** (2020), 125–183. https://arxiv.org/abs/1904.03395
3. OEIS Foundation, A000085 (involution numbers). https://oeis.org/A000085
