# Exact two-sum spectra and dyadic additive energy of odd Pascal-row positions

## Finding
For each integer \(n\ge0\), define the odd-coefficient support of its Pascal row by
\[
A_n=\{k\in\mathbb Z:0\le k\le n,\ \binom{n}{k}\equiv1\pmod2\}.
\]
Define the *ordered two-sum representation function* and its ordinary-integer additive energy by
\[
R_n(t)=\#\{(a,b)\in A_n^2:a+b=t\},\qquad E(n)=\sum_{t\in\mathbb Z}R_n(t)^2.
\]
If the nonnegative integer \(n\) has maximal binary runs of ones with starting positions \(h_i\) and positive lengths \(\ell_i\) (the least significant bit has position zero), put \(m_i=2^{\ell_i}\), for \(1\le i\le s\). Then every supported sum \(t\) has the unique representation
\[
t=\sum_{i=1}^s2^{h_i}v_i,\qquad 0\le v_i\le2m_i-2,
\]
and on this support its multiplicity is exactly
\[
\boxed{R_n(t)=\prod_{i=1}^s\min\{v_i+1,2m_i-1-v_i\}.}
\]
All other integer arguments have multiplicity zero. Therefore
\[
\boxed{E(n)=\prod_{i=1}^s\frac{2\cdot8^{\ell_i}+2^{\ell_i}}{3}.}
\]
For the empty list of runs, representing \(n=0\), both products are one.

The dyadic total \(F_r=\sum_{n=0}^{2^r-1}E(n)\), defined for every integer \(r\ge0\), has the exact rational generating function
\[
\boxed{\sum_{r\ge0}F_rz^r=\frac{1-4z}{1-11z+20z^2}.}
\]
In particular, \(F_0=1\), \(F_1=7\), and \(F_r=11F_{r-1}-20F_{r-2}\) for \(r\ge2\). The first values are \(1,7,57,487,4217,36647\). Defining \(\lambda_\pm=(11\pm\sqrt{41})/2\), the exact formula is
\[
F_r=\frac{1+3/\sqrt{41}}2\lambda_+^r+\frac{1-3/\sqrt{41}}2\lambda_-^r,
\]
so the leading growth is \(\tfrac12(1+3/\sqrt{41})\lambda_+^r\).

## Assumptions and scope
All sums use ordinary integer addition, not coordinatewise addition of binary vectors. Ordered pairs and ordered quadruples are counted, with no requirement that their entries be distinct. The energy counts quadruples \((a,b,c,d)\in A_n^4\) satisfying \(a+b=c+d\). Binary runs are maximal and therefore separated by at least one zero bit. The definitions cover \(n=0\) and \(r=0\).

## Proof
**1. The row support splits into full binary-run blocks.** Lucas's theorem modulo two states that \(\binom nk\) is odd exactly when every one-bit of \(k\) is a one-bit of \(n\). Consequently every \(a\in A_n\) has a unique representation
\[
a=\sum_{i=1}^s2^{h_i}u_i,\qquad 0\le u_i<m_i.
\]
Each \(u_i\) uses exactly the allowed bits in its consecutive run.

**2. Distinct block-sum vectors yield distinct integers.** Adding two support elements gives \(t=\sum_i2^{h_i}v_i\) with \(0\le v_i\le2m_i-2\). Suppose two such digit vectors gave the same integer; take the largest starting position \(h_i\) where they differ. Its contribution to the difference has magnitude at least \(2^{h_i}\). The absolute value of the contribution from smaller starting positions is at most
\[
\sum_{j<i}(2m_j-2)2^{h_j}=2\sum_{j<i}\sum_{k=h_j}^{h_j+\ell_j-1}2^k<2^{h_i},
\]
because all one-bit positions of earlier blocks lie below \(h_i-1\), leaving a full zero bit before \(h_i\). This is a contradiction. The same reasoning includes the empty-run case.

**3. Exact convolution fibers and energy.** In a block of size \(m\), the number of ordered pairs \((u,u')\in\{0,\ldots,m-1\}^2\) with \(u+u'=v\) is
\[
\rho_m(v)=\min\{v+1,2m-1-v\}\quad(0\le v\le2m-2).
\]
Step 2 makes every global sum-vector unambiguous, and independent block choices multiply. Hence the announced product for \(R_n(t)\) follows. By separating the unique peak at \(v=m-1\),
\[
\sum_{v=0}^{2m-2}\rho_m(v)^2=m^2+2\sum_{q=1}^{m-1}q^2=\frac{2m^3+m}{3}.
\]
Multiplication over the runs, substituting \(m_i=2^{\ell_i}\), yields the exact energy formula.

**4. Dyadic run enumeration.** Set \(f(\ell)=(2\cdot8^\ell+2^\ell)/3\) for \(\ell\ge1\). Binary strings of length \(r\) represent the integers \(0\le n<2^r\), with leading zero bits allowed. A string is empty, begins with zero, begins with a run of ones followed by a zero, or consists entirely of ones. With
\[
W(z)=\sum_{\ell\ge1}f(\ell)z^\ell=\frac{6z-16z^2}{1-10z+16z^2},\qquad F(z)=\sum_{r\ge0}F_rz^r,
\]
this exhaustive disjoint decomposition gives the formal-power-series identity
\[
F(z)=1+zF(z)+W(z)+zW(z)F(z).
\]
Solving,
\[
F(z)=\frac{1+W(z)}{1-z-zW(z)}=\frac{1-4z}{1-11z+20z^2}.
\]
The recurrence and closed form follow by coefficient comparison and the two distinct roots of the denominator. Since \(\lambda_+>\lambda_->0\) and its coefficient is positive, the stated leading growth is valid for all integer \(r\to\infty\).

## Verification
The standalone file `verification/verify.py` checks Lucas parity against exact binomial coefficients for 32,896 cases, compares full ordered two-sum multiplicity profiles and energies for each of the 256 rows indexed \(0\le n<256\), and checks the dyadic recurrence at 12 levels through \(r=11\), representing 2,048 rows. Invoke `python3 verification/verify.py` from the extracted package root. These finite tests diagnose implementation and boundary mistakes; the proof above, not these tests, establishes the universal statements.

## Relationship to prior work
Mathonet, Rigo, Stipulanti and Zénaïdi study digital encodings of Pascal rows modulo primes [1], including the support structure underlying the first proof step. Wu develops run-length transforms for other sums of products of binomial coefficients modulo two [2]. Rampersad and Wiebe study related run-length transforms, regularity, and some aggregate identities [3]. Their methods motivate the present run-block approach but the particular ordinary-integer two-sum multiplicity formula, exact energy, and dyadic rational generating function are not stated in the portions of those primary texts inspected. In particular, known vector-cube energy identities do not directly cover ordinary-integer sums: the carries within a run give \(E(3)=44\), whereas a two-dimensional binary vector cube has energy \(36\).

## Limitations
The result is restricted to parity of binomial coefficients, ordinary *two*-sums and their fourth-moment energy. No assertion is made about higher moments or odd-prime digit restrictions. The relation to preexisting general run-length-transform methods may allow an alternative, perhaps implicit derivation; lack of a matching database or literature hit is not proof of absolute novelty. The mathematical result has not undergone independent scientific validation.

## References
[1] P. Mathonet, M. Rigo, M. Stipulanti, N. Zénaïdi, *On digital sequences associated with Pascal's triangle*, arXiv:2201.06636, first posted 17 January 2022. https://arxiv.org/abs/2201.06636

[2] C. W. Wu, *Sums of products of binomial coefficients mod 2 and run length transforms of sequences*, arXiv:1610.06166, first posted 19 October 2016. https://arxiv.org/abs/1610.06166

[3] N. Rampersad, M. Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012, first posted 7 September 2023. https://arxiv.org/abs/2309.04012
