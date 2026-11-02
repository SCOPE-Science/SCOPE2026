# Exact good-prime-power images and p-adic density of pentatope numbers

## Finding

The fourth binomial coefficient \(P(x)=\binom{x}{4}\), whose nonnegative integer values are pentatope (four-simplex) numbers, has an explicit image modulo every power of every prime \(p\ge7\). The formula gives the exact number of attained residues at every depth and the limiting measure of the image in \(\mathbb Z_p\). Its only nontrivial lifting obstructions arise from two arithmetically distinguishable critical values.

For a prime \(p\ge7\), write \(\chi_p\) for the Legendre symbol (with \(\chi_p(0)=0\)). Set
\[
T_p=\frac{3p+4+\chi_p(-1)+2\chi_p(5)-2\chi_p(10)}8,
\qquad
 e_p=\frac{1+\chi_p(5)}2+\frac{1-\chi_p(10)}2.
\]
For \(m\ge0\), write \(S_p(m)\) for the number of squares, including zero, in \(\mathbb Z/p^m\mathbb Z\), with \(S_p(0)=1\). Explicitly,
\[
S_p(m)=1+\frac{p-1}{2}\sum_{j=0}^{\lfloor(m-1)/2\rfloor}p^{m-2j-1}\quad(m\ge1).
\]
Then for \(V_{p,k}=\{P(n)\bmod p^k:n\ge0\}\),
\[
\boxed{\ |V_{p,1}|=T_p,\qquad
|V_{p,k}|=(T_p-e_p)p^{k-1}+e_pS_p(k-2)\ \ (k\ge2).\ }
\]
Its normalized additive Haar measure satisfies
\[
\boxed{\ \mu_p(P(\mathbb Z_p))
=\frac{T_p-e_p}{p}+\frac{e_p}{2p(p+1)}.\ }
\]
In particular, the measure approaches \(3/8\) as \(p\) tends to infinity through primes.

## Assumptions and scope

Every prime is at least seven, so \(2\), \(3\), \(5\), \(24\), \(48\), \(128\), and \(384\) are units in the relevant \(p\)-adic ring. All rational constants below therefore belong to \(\mathbb Z_p\). Let
\[
 c_0=\frac3{128},\qquad c_1=-\frac1{24},\qquad
 \alpha_0=-\frac5{48},\qquad \alpha_1=\frac1{24}.
\]
Define \(I_p=P(\mathbb F_p)\), understood through reduction of the integer-coefficient polynomial \(P\). Let
\[
E_p=\big(\{\overline{c_0}\}\text{ if }\chi_p(10)=-1\big)
\cup\big(\{\overline{c_1}\}\text{ if }\chi_p(5)=1\big),
\]
where a conditional set is empty when its displayed condition fails. The two residues are distinct since \(c_0-c_1=25/384\) is a unit.

The complete image, as a set rather than merely a count, is
\[
\boxed{
P(\mathbb Z_p)=
\bigcup_{r\in I_p\setminus E_p}(r+p\mathbb Z_p)
\ \cup\ \begin{cases}c_0+\alpha_0(p\mathbb Z_p)^2,&\chi_p(10)=-1,\\\varnothing,&\chi_p(10)=1\end{cases}
\ \cup\ \begin{cases}c_1+\alpha_1(p\mathbb Z_p)^2,&\chi_p(5)=1,\\\varnothing,&\chi_p(5)=-1.\end{cases}
}
\]
Here a residue \(r\) in a residue ball is represented by any integer lift; \((p\mathbb Z_p)^2\) means the set of squares of elements divisible by \(p\), not the ideal \(p^2\mathbb Z_p\). Reduction of this identity modulo \(p^k\) explicitly determines which individual residues occur. The theorem does not discuss the bad primes \(2,3,5\).

## Proof

**1. A nested-square normal form.** Put \(u=x-3/2\). Direct factorization gives
\[
P(x)=\frac{(u^2-1/4)(u^2-9/4)}{24},
\qquad 24P(x)+1=(u^2-5/4)^2.
\]
Thus \(24P'(x)=4u(u^2-5/4)\). Its only possible critical points modulo \(p\) are \(u=0\) and the roots of \(u^2=5/4\), and their respective values are \(c_0\) and \(c_1\).

**2. Exact finite-field value-set count.** The map \(u\mapsto u^2\) has image \(Q\subset\mathbb F_p\), the squares including zero, with \(|Q|=(p+1)/2\). By the nested-square identity, two \(t,t'\in Q\) have the same final value precisely when \(t'=t\) or \(t'=5/2-t\). Set \(c=5/2\), let \(J=|Q\cap(c-Q)|\), and let \(F\) be one if \(5/4\in Q\), zero otherwise. These are the number of paired elements and the number of fixed elements of the reflection, so
\[
|I_p|=|Q|-(J-F)/2.
\]
Since \(\mathbf 1_Q(t)=(1+\chi_p(t)+\mathbf 1_{t=0})/2\), expansion and the elementary quadratic-character identity \(\sum_t\chi_p(t(c-t))=-\chi_p(-1)\) for \(c\ne0\) give
\[
J=\frac{p+2+2\chi_p(10)-\chi_p(-1)}4,
\qquad F=\frac{1+\chi_p(5)}2.
\]
Substitution gives \(|I_p|=T_p\). This is a specialization of the established finite-field Dickson-polynomial value-set phenomenon, not an assertion that the prime-field component is new.

**3. Regular balls.** If \(r\in I_p\) and \(r\notin\{\overline{c_0},\overline{c_1}\}\), every preimage is nonsingular, so Hensel's lemma gives \(r+p\mathbb Z_p\subset P(\mathbb Z_p)\). At \(\overline{c_0}\), the equation \(P(x)=c_0\) becomes \(u^2(u^2-5/2)=0\) modulo \(p\). If \(\chi_p(10)=1\), it has nonsingular preimages from \(u^2=5/2\), hence the whole ball is again attained. If \(\chi_p(10)=-1\), its only preimage is the singular root \(u=0\). At \(\overline{c_1}\), the equation is \((u^2-5/4)^2=0\); this residue has a preimage exactly if \(\chi_p(5)=1\), and all such preimages are singular. Consequently, the exceptional classes are precisely \(E_p\), and \(|E_p|=e_p\).

**4. The singular balls are scaled square sets.** If \(\chi_p(10)=-1\), every preimage of \(\overline{c_0}\) has \(u\in p\mathbb Z_p\). The exact identity
\[
P(x)-c_0=\alpha_0 u^2\left(1-\frac25u^2\right)
\]
shows that the unit factor in parentheses has a unique square root congruent to one modulo \(p\). The change \(v=u\sqrt{1-2u^2/5}\) is a bijection from \(p\mathbb Z_p\) onto itself: it is congruent to \(u\) modulo \(p^2\) and has unit derivative, so the inverse exists by Hensel lifting (equivalently, by successive digit lifting). Hence exactly \(c_0+\alpha_0(p\mathbb Z_p)^2\) occurs in this class.

If \(\chi_p(5)=1\), the equation \(u^2=5/4\) has two distinct Hensel roots in \(\mathbb Z_p\), and for \(u\) in either of their residue balls the map \(u\mapsto u^2-5/4\) maps that ball bijectively onto \(p\mathbb Z_p\). The identity
\[
P(x)-c_1=\frac{(u^2-5/4)^2}{24}
\]
therefore shows that exactly \(c_1+\alpha_1(p\mathbb Z_p)^2\) occurs in the second exceptional class. As the two exceptional residue classes are distinct, the set decomposition follows.

**5. Counting the lifts.** Every regular ball contains \(p^{k-1}\) residue classes modulo \(p^k\). For \(k\ge2\), a singular square ball \(c+\alpha(p\mathbb Z_p)^2\) contains \(S_p(k-2)\) residue classes modulo \(p^k\). The displayed formula for \(S_p(m)\) follows by sorting square residues according to their even \(p\)-adic valuation: each valuation \(2j<m\) contributes \((p-1)p^{m-2j-1}/2\) classes and zero contributes one. This proves the exact size formula for every \(k\).

**6. Haar measure.** A unit is a square with relative frequency \(1/2\); therefore the normalized measure of squares in \(\mathbb Z_p\) is
\[
\sum_{j\ge0}\frac{p-1}{2p}p^{-2j}=\frac{p}{2(p+1)}.
\]
Each singular square ball has measure \(p^{-2}\cdot p/[2(p+1)]=1/[2p(p+1)]\), and each regular ball has measure \(1/p\). Adding the disjoint contributions proves the measure formula. Finally \(T_p=3p/8+O(1)\) and \(e_p\le2\), giving the stated asymptotic.

## Verification

The standalone program `artifacts/verify.py` independently constructs the full value set by evaluating the integer polynomial on every residue modulo selected prime powers. It separately constructs the predicted union of regular residue balls and two possible scaled-square balls and checks equality of the entire sets, not only equality of cardinalities. It also checks the closed formula for \(S_p(m)\) and the resulting image count.

Run `python3 artifacts/verify.py` with Python 3 and no third-party dependencies. On the recorded run it reported `VERIFY_OK cases=34 fully_enumerated_inputs=337286 complete_set_matches`. The checked primes are \(7,11,13,17,19,23,29,31,37,41\), with every exponent from one through four for which the modulus is at most \(120000\). Examples include \(|V_{7,4}|=708\) and \(|V_{11,4}|=4105\). These finite verifications do not prove the statement for all prime powers; the preceding algebraic, character-sum, and lifting arguments do.

## Relationship to prior work

The polynomial is an affine transform of the fourth Dickson polynomial: with \(a=5/8\),
\[
24P(x)=D_4(x-3/2,a)-7/32,
\qquad D_4(u,a)=u^4-4au^2+2a^2.
\]
The arithmetic under study therefore lies within the classical Dickson-polynomial literature. Chou, Gomez-Calderon, and Mullen (1988) determine finite-field Dickson value-set cardinalities, covering the prime-field counting aspect in principle. Bremser and Gomez-Calderon (1991) study Dickson-polynomial images over Galois rings and give estimates and preimage results, so their work is the closest potentially stronger comparison. The present claim is the explicit set-level classification and exact all-depth prime-power cardinality/measure formula for the pentatope polynomial at every good prime. General finite-field value-set estimates such as Mullen, Wan, and Wang (2012) do not furnish this prime-power classification.

## Limitations

The prime \(5\) is excluded because the two critical values coalesce modulo that prime, and \(2,3\) are excluded because of denominators. Their image structures are not determined here. The finite-field value-set component is an established Dickson-polynomial specialization. The exact comparison with all consequences of the 1991 Galois-ring article is not resolved because only its abstract was accessible; historical priority of the prime-power refinement remains qualified. No assertion is made about arbitrary quartic polynomials or nonprime-power moduli, and no independent audit is claimed.

## References

1. W. S. Chou, J. Gomez-Calderon, and G. L. Mullen, *Value sets of Dickson polynomials over finite fields*, Journal of Number Theory 30 (1988), 334–344, DOI: 10.1016/0022-314X(88)90006-6.
2. P. S. Bremser and J. Gomez-Calderon, *Value sets of Dickson polynomials over Galois rings*, Journal of Number Theory 38 (1991), 240–250, DOI: 10.1016/0022-314X(91)90087-R.
3. G. L. Mullen, D. Wan, and Q. Wang, *Value sets of polynomial maps over finite fields*, arXiv:1210.8119v1 (first public version dated 2012-10-30), DOI: 10.48550/arXiv.1210.8119.
4. W. J. Ralph, *The value set of polynomials over \(\mathbb Z_m\) and the combinatorics of sequences*, Mathematika 42 (1995), 190–198, DOI: 10.1112/S0025579300011487.
5. OEIS A000332, the sequence of pentatope numbers.
