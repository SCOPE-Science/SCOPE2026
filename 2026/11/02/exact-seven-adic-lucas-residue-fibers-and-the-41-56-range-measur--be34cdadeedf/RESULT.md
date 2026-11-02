# Exact seven-adic Lucas residue fibers and the \(41/56\) range measure

## Finding

Let the Fibonacci and Lucas sequences be defined, for nonnegative integers \(n\), by
\[
F_0=0,\quad F_1=1,\qquad L_0=2,\quad L_1=1,\qquad
U_{n+2}=U_{n+1}+U_n
\]
for either sequence \(U\). For \(k\ge1\) put \(P_k=16\cdot7^{k-1}\), and for \(y\in\mathbb Z/7^k\mathbb Z\) define
\[
v_k(y)=\#\{0\le n<P_k:L_n\equiv y\pmod{7^k}\}.
\]

**Theorem.** The Lucas sequence has least period \(P_k\) modulo \(7^k\). Its complete residue-frequency distribution is as follows.

For every \(k\ge1\), if \(y\bmod7\) belongs to \(\{0,1,3,4,6\}\), then
\[
\begin{array}{c|ccccc}
y\bmod7&0&1&3&4&6\\\hline
v_k(y)&2&2&4&4&2
\end{array}.
\]
At \(k=1\) the two remaining residues, \(2\) and \(-2\) modulo \(7\), each have frequency one. At \(k\ge2\), the only additional possible targets satisfy \(y\equiv2\) or \(y\equiv-2\pmod{49}\). For these targets set \(j=k-2\), and define
\[
s_y\equiv\frac{y^2-4}{5\cdot7^2}\pmod{7^j},\qquad
R_j(s)=\#\{z\bmod7^j:z^2\equiv s\pmod{7^j}\}.
\]
The quotient defining \(s_y\) is well defined because \(49\mid y^2-4\) and \(5\) is invertible. For \(j=0\) the trivial ring is understood and \(R_0(0)=1\). Then
\[
\boxed{\ v_k(y)=7R_{k-2}(s_y)\qquad(k\ge2,\ y\equiv\pm2\pmod{49}).\ }
\]
Every target not covered by these cases has frequency zero. Explicitly, for \(j\ge1\),
\[
R_j(s)=
\begin{cases}
7^{\lfloor j/2\rfloor},&s\equiv0\pmod{7^j},\\
2\cdot7^h,&\nu_7(s)=2h<j\text{ and }7^{-2h}s\text{ is a quadratic residue modulo }7,\\
0,&\text{otherwise}.
\end{cases}
\]
In the middle case, \(7^{-2h}s\) refers to the unit factor of an integer representative of \(s\).

Writing \(Q_0=1\) and, for \(j\ge1\),
\[
Q_j=1+\sum_{h=0}^{\lfloor(j-1)/2\rfloor}3\cdot7^{j-2h-1},
\]
the number of distinct residues among the Lucas numbers modulo \(7^k\) is
\[
\boxed{\ N_k=5\cdot7^{k-1}+2Q_{\max(k-2,0)}.\ }
\]
Thus \(N_1,N_2,N_3,N_4,N_5,N_6=7,37,253,1759,12307,86137\).

In the ring of seven-adic integers, let \(\mathbb Z_7^2=\{z^2:z\in\mathbb Z_7\}\) (notation here means the *square-value set*, not a Cartesian product). The closure of \(\{L_n:n\ge0\}\) is the disjoint union of the five full residue disks \(y\bmod7\in\{0,1,3,4,6\}\) and
\[
2+\frac54\,7^2\mathbb Z_7^2
\quad\text{and}\quad
-2-\frac54\,7^2\mathbb Z_7^2.
\]
Its normalized additive Haar measure is exactly \(\boxed{41/56}\).

## Assumptions and scope

All periods and frequencies are for the Lucas recurrence with the given initial values, not arbitrary second-order recurrences. The modulus is a positive power of the fixed prime \(7\). A length-\(P_k\) period counts indices beginning at zero. The valuation \(\nu_7\) of zero is treated separately. The formulas hold at every integer \(k\ge1\); the special handling of \(k=1\) is essential.

## Proof

**1. Exact period and lifting.** Let
\[
M=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
Direct recurrence multiplication gives
\[
M^8=\begin{pmatrix}34&21\\21&13\end{pmatrix}\equiv-I\pmod7,
\qquad
M^{16}=\begin{pmatrix}1597&987\\987&610\end{pmatrix}
=I+7\begin{pmatrix}228&141\\141&87\end{pmatrix}.
\]
Consequently \(M\) has order exactly \(16\) modulo \(7\), and the matrix \((M^{16}-I)/7\) has a unit off-diagonal entry modulo \(7\). Standard binomial lifting for odd primes proves that \(M^{16\cdot7^h}\) is \(I\) modulo \(7^{h+1}\), but not modulo \(7^{h+2}\), for every \(h\ge0\). Hence the order of \(M\) modulo \(7^k\) is \(16\cdot7^{k-1}\).

For the Lucas state vector \(v=(L_1,L_0)^T=(1,2)^T\), the determinant of the two columns \(v,Mv\) is \(-5\), a unit modulo every \(7^k\). If \(M^d v=v\), then commutation gives \(M^d(Mv)=Mv\), and therefore \(M^d=I\). Thus the Lucas scalar sequence has the same *least* period \(P_k\) as \(M\).

More precisely, for every nonzero integer \(d\), off-diagonal binomial lifting gives
\[
\nu_7(F_{16d})=1+\nu_7(d).
\tag{1}
\]
For \(d<0\), use \(F_{-m}=(-1)^{m+1}F_m\). The identity
\[
L_m^2-5F_m^2=4(-1)^m
\tag{2}
\]
and \(L_{16d}\equiv2\pmod7\) imply
\[
\nu_7(L_{16d}-2)=2+2\nu_7(d).
\tag{3}
\]
Here \(L_{16d}+2\equiv4\pmod7\) is a unit. All equalities are exact valuations, not estimates.

**2. The nonsingular disks.** For any integer \(n\) and any even integer \(h\), addition identities give
\[
2(L_{n+h}-L_n)=(L_h-2)L_n+5F_hF_n,
\qquad
2(F_{n+h}-F_n)=(L_h-2)F_n+F_hL_n.
\tag{4}
\]
The sixteen pairs \((L_a,F_a)\bmod7\), for \(0\le a<16\), are obtained directly from the recurrence. The only positions with \(F_a\equiv0\pmod7\) are \(a=0,8\). Their Lucas residues are \(2,-2\), respectively. All other fourteen positions have Lucas residues with multiplicities \(2,2,4,4,2\) at \(0,1,3,4,6\), respectively.

For \(a\notin\{0,8\}\), take \(n=a+16t\) and \(h=16(t'-t)\). Since \(F_n\) is a unit and the first term on the right of the Lucas identity in (4) has valuation at least \(2+2\nu_7(t'-t)\), while its second term has valuation exactly \(1+\nu_7(t'-t)\),
\[
\nu_7(L_{a+16t'}-L_{a+16t})=1+\nu_7(t'-t).
\tag{5}
\]
Therefore \(t\mapsto(L_{a+16t}-L_a)/7\) induces an isometry, and hence a bijection, on \(\mathbb Z/7^{k-1}\mathbb Z\). Each nonsingular branch covers its full Lucas residue disk, once per target. Summing branches proves all five stated constant regular frequencies.

**3. Two quadratic disks.** Fix \(a=0\) or \(8\). Since \(F_{a+16t}\equiv0\) and \(L_{a+16t}\equiv\pm2\pmod7\), the second identity in (4), together with (1) and (3), gives
\[
\nu_7(F_{a+16t'}-F_{a+16t})=1+\nu_7(t'-t).
\tag{6}
\]
Consequently the normalized map \(t\mapsto F_{a+16t}/7\) is a bijection modulo \(7^j\) when \(t\) ranges modulo \(7^j\), for every \(j\ge0\).

Every index in either critical branch is even. Thus (2) becomes \(L_n^2=4+5F_n^2\). At \(k\ge2\), the Lucas value must satisfy \(y\equiv\pm2\pmod{49}\). Fix such a \(y\), and let \(j=k-2\). If \(L_{a+16t}\equiv y\pmod{7^k}\), then
\[
\left(F_{a+16t}/7\right)^2\equiv
(y^2-4)/(5\cdot7^2)\pmod{7^j}.
\tag{7}
\]
Conversely, if (7) holds, the square identity yields \(L_{a+16t}^2\equiv y^2\pmod{7^k}\). Since their reductions modulo \(7\) have the same prescribed sign \(\pm2\), their sum is a unit, so \(L_{a+16t}\equiv y\pmod{7^k}\). By (6), each of the \(R_j(s_y)\) square roots modulo \(7^j\) has exactly \(7\) index parameters \(t\) modulo \(7^{k-1}\). This proves the exact critical-fiber formula. At \(k=1\), each critical branch consists of a single index modulo \(P_1\), giving multiplicity one.

**4. Support and limiting measure.** Squares modulo \(7^j\) are zero or have even valuation \(2h<j\), with one of three nonzero quadratic-residue unit leading digits. This gives the displayed formula for \(R_j(s)\) and the number \(Q_j\) of square residues. Each of the two critical branches has exactly \(Q_{k-2}\) distinct targets for \(k\ge2\), and the other five residue disks contribute \(5\cdot7^{k-1}\) targets, establishing \(N_k\).

In \(\mathbb Z_7\), every unit congruent to \(1\pmod7\) is a square. For \(y=2+49w\), the condition \((y^2-4)/(5\cdot49)\in\mathbb Z_7^2\) is equivalent to \((4/5)w\in\mathbb Z_7^2\), because the extra factor \((y+2)/4\) lies in \(1+7\mathbb Z_7\) and is a square. Similarly, near \(-2\) the critical set is \(-2-(5/4)49\mathbb Z_7^2\). The set of squares in \(\mathbb Z_7\) has additive Haar measure
\[
\sum_{h=0}^{\infty}\frac{3}{7^{2h+1}}=\frac7{16}.
\]
The five full residue disks have total measure \(5/7\), and each quadratic disk has measure \((7/16)/49\). Hence the total measure is
\[
\frac57+\frac{2}{49}\frac7{16}=\boxed{\frac{41}{56}}.
\]
The finite congruence support formulas are compatible across \(k\), so this is exactly the closure of the nonnegative-index Lucas values. This completes the proof.

## Verification

A standalone Python program, `artifacts/verify_lucas7.py`, independently iterates the defining Lucas recurrence through its least period at all moduli \(7^k\) for \(1\le k\le6\). It compares every resulting residue frequency with the formula and checks matrix orders and image cardinalities. Its observed final line is `VERIFY_OK full_fibers=137256 levels=1..6 minimal_periods_and_exact_multiplicities`. Computation only checks finite levels; the proof above establishes all \(k\).

## Relationship to prior work

Lang and Lang (arXiv:1304.2892, first posted April 10, 2013) classify *residue completeness* of Fibonacci-type cycles, including the fact that Lucas numbers are complete modulo \(7\) but not \(7^k\) for \(k\ge2\). That result does not determine which residues survive or their frequencies. Somer and Carlip's earlier stability work (2000) gives general frequency bounds and nonstability criteria for companion Lucas recurrences, but not this explicitly evaluated all-level prime-seven fiber formula. Carlip and Somer (2007) analyze additional p-singular frequency behavior; their Theorem 6.1 assumes a parameter \(e>1\), whereas the present matrix has the first lift at exponent one. Bundschuh and Bundschuh give complete analogous distributions at primes \(2,5\) (2010) and \(3\) (2011). None of the inspected statements explicitly covers this all-level prime-seven classification. Patel and Shah (2021) give a one-/two-/four-block statement for Lucas periods in their abstract; their full paper was not accessible, so no implication about exact seven-power fibers is asserted. The possibility of another specialized source or a nontrivial reduction from a more general theorem remains an originality risk.

## Limitations

Only the fixed Lucas recurrence and the prime \(7\) are treated. This is not a classification for arbitrary Lucas parameters or arbitrary prime powers. The Haar measure concerns the *seven-adic closure of attained values*, not the density of indices satisfying a fixed congruence. Finite verification is not a replacement for the all-level proof. The historical novelty claim is qualified and has not undergone independent review.

## References

1. C. L. Lang and M. L. Lang, *Fibonacci system and residue completeness*, arXiv:1304.2892 (first posted 2013-04-10), https://arxiv.org/abs/1304.2892.
2. L. Somer and W. Carlip, *Stability of second-order recurrences modulo prime powers*, International Journal of Mathematics and Mathematical Sciences 23 (2000), DOI:10.1155/S0161171200003240.
3. W. Carlip and L. Somer, *Bounds for frequencies of residues of second-order recurrences modulo prime powers*, Mathematica Bohemica 132 (2007), 137–175, DOI:10.21136/MB.2007.134189.
4. P. Bundschuh and R. Bundschuh, *The sequence of Lucas numbers is not stable modulo 2 and 5*, Uniform Distribution Theory 5 (2010), 113–130, https://pcwww.liv.ac.uk/~karpenk/JournalUDT/vol05/no2/6Bundsch10-2.pdf.
5. R. Bundschuh and P. Bundschuh, *Distribution of Fibonacci and Lucas numbers modulo powers of 3*, Fibonacci Quarterly 49 (2011), 201–210, DOI:10.1080/00150517.2011.12428042.
6. C. Sanna, *The p-adic valuation of Lucas sequences*, Fibonacci Quarterly 54 (2016), 118–124.
7. R. P. Patel and D. V. Shah, *Blocks within the period of Lucas sequence*, Ratio Mathematica 41 (2021), DOI:10.23755/rm.v41i0.664 (abstract accessed; full text gated).
