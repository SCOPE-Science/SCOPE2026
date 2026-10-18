# Exact two-sum fibers and fourth moments for prime-power modular hyperbolas

## Finding

Let \(p\) be any odd prime, \(k\ge 2\), \(N=p^k\), \(R=\mathbb Z/N\mathbb Z\), and \(U=R^\times\). Put \(m=(p-1)p^{k-1}\) and
\[
H=\{(x,x^{-1}):x\in U\}\subset R^2,\qquad
r(s,z)=\#\{(x,y)\in U^2:x+y=s,\ x^{-1}+y^{-1}=z\}.
\]
For each fixed \(s\in R\), the complete **positive-fiber census** of \(r(s,z)\), as \(z\) varies through \(R\), is:

* \(s=0\): the sole positive fiber is \(r(0,0)=m\).
* \(v_p(s)=a\) with \(1\le a<k\): precisely \((p-1)p^{k-a-1}/2\) fibers have size \(2p^a\).
* \(s\in U\): exactly \((p-3)p^{k-1}/2\) fibers have size \(2\); for each \(1\le j\le\lfloor(k-1)/2\rfloor\), precisely \((p-1)p^{k-2j-1}/2\) fibers have size \(2p^j\); and exactly **one** fiber has size \(p^{\lfloor k/2\rfloor}\).

All remaining fibers are zero. In particular, with \(E(H)=\sum_{s,z\in R}r(s,z)^2\),
\[
\boxed{E(H)=3(p-1)p^{2k-2}\bigl(k(p-1)-1\bigr).}
\]
If
\[
K_N(u,v)=\sum_{x\in U}\exp\!\left(\frac{2\pi i(ux+vx^{-1})}N\right),
\]
then orthogonality gives the **two-parameter fourth moment**
\[
\boxed{\sum_{u,v\in R}|K_N(u,v)|^4=N^2E(H)
=3(p-1)p^{4k-2}\bigl(k(p-1)-1\bigr).}
\]
For normalized Fourier synthesis \(\mathcal E\mathbf1=K_N/m\), with unnormalized counting measure on \(R^2\), this becomes
\[
\sum_{u,v\in R}|\mathcal E\mathbf1(u,v)|^4
=\frac{3p^2\bigl(k(p-1)-1\bigr)}{(p-1)^3}.
\]
The result concerns the **complete fiber distribution** and the constant-input fourth moment, not the sharp \(L^2\to L^4\) operator norm.

## Assumptions and scope

Arithmetic is in the residue ring \(R=\mathbb Z/p^k\mathbb Z\), not in the finite field \(\mathbb F_{p^k}\). The valuation \(v_p(s)\) is defined on residues by \(v_p(0)=k\) and \(0\le v_p(s)<k\) otherwise. All pair counts are **ordered**. Both the prime \(p\) and the exponent \(k\) are unrestricted in the stated odd-prime, \(k\ge2\) range. The prime-modulus \(k=1\) situation is not asserted as a new contribution. The exponential has the positive sign convention; the fourth-power identity is independent of sign.

## Proof

**1. The zero-sum fiber.** If \(x+y=0\), then \(y=-x\) and \(x^{-1}+y^{-1}=0\), for every unit \(x\). Hence \(r(0,0)=m\) and the remaining fibers in that row vanish.

**2. Nonzero nonunits.** Let \(s=p^a s_0\), where \(1\le a<k\) and \(s_0\) is a unit modulo \(p^{k-a}\). Since \(x+y=s\), both \(x\) and \(y=s-x\) must be units with opposite nonzero residues modulo \(p\). Since \(z=(x+y)/(xy)\), a nonzero fiber requires \(z=p^a z_0\) with \(z_0\in(\mathbb Z/p^{k-a}\mathbb Z)^\times\), and reduces to
\[
x(s-x)\equiv s_0z_0^{-1}\pmod{p^{k-a}}.
\]
Modulo \(p\), this is \(x^2\equiv -s_0z_0^{-1}\). It has two simple roots exactly when the Legendre symbol \(\chi_p(-s_0z_0^{-1})=1\), and otherwise none. Hensel lifting gives exactly two roots modulo \(p^{k-a}\) in the former case. Each lifts to \(p^a\) residues \(x\) modulo \(p^k\), with \(y=s-x\) uniquely determined. As \(z_0\) runs over the units modulo \(p^{k-a}\), exactly half give square discriminant: \((p-1)p^{k-a-1}/2\) distinct positive fibers, each of size \(2p^a\). All other \(z\) give zero.

**3. Unit sums.** Let \(s\in U\). If a fiber is nonzero, \(z=s/(xy)\) is a unit. Eliminate \(y=s-x\) and complete the square:
\[
x^2-sx+sz^{-1}\equiv0\pmod N,
\qquad (2x-s)^2\equiv\Delta\pmod N,
\quad\Delta=s^2-4sz^{-1}.
\]
The map \(z\mapsto\Delta\) is a bijection between the units \(z\in U\) and the residues \(\Delta\) with \(\Delta\not\equiv s^2\pmod p\), with inverse \(z=4s(s^2-\Delta)^{-1}\). The roots \(x\) recovered from \(2x-s\) are all units, as are \(s-x\), because their product \(sz^{-1}\) is a unit. Thus \(r(s,z)\) is exactly the number of square roots of \(\Delta\) modulo \(p^k\).

For odd \(p\), the root count is \(2\) when \(\Delta\) is a quadratic-residue unit; \(2p^j\) when \(v_p(\Delta)=2j<k\) and its reduced unit is a quadratic residue; \(p^{\lfloor k/2\rfloor}\) when \(\Delta=0\); and \(0\) otherwise. Removing the single prohibited nonzero square residue class \(s^2\pmod p\) leaves \((p-3)p^{k-1}/2\) unit-square \(\Delta\). At valuation \(2j\) the count of admissible \(\Delta\) is \((p-1)p^{k-2j-1}/2\). Finally \(\Delta=0\) contributes one fiber of size \(p^{\lfloor k/2\rfloor}\). These are precisely the asserted unit-row strata.

**4. Energy.** The zero row contributes \(m^2\). Each nonunit valuation layer \(a=1,\ldots,k-1\) contains \((p-1)p^{k-a-1}\) choices of \(s\), each having \((p-1)p^{k-a-1}/2\) positive \(z\)-fibers of size \(2p^a\). The energy of each layer is therefore \(2m^2\). For a fixed unit \(s\), the root multiplicities in Step 3 give
\[
\sum_{z\in R}r(s,z)^2
=2(p-3)p^{k-1}+2(p-1)p^{k-1}\left\lfloor\frac{k-1}2\right\rfloor
+p^{2\lfloor k/2\rfloor}
=p^{k-1}\bigl((k+1)(p-1)-3\bigr).
\]
The last identity is valid in both parity cases for \(k\). Summing over the \(m\) units \(s\), and adding the zero and nonunit rows, yields
\[
\begin{aligned}
E(H)&=m\,p^{k-1}\bigl((k+1)(p-1)-3\bigr)
 +(2k-1)m^2\\
&=3(p-1)p^{2k-2}\bigl(k(p-1)-1\bigr).
\end{aligned}
\]

**5. Fourier fourth moment.** Expand \(|K_N(u,v)|^4\), sum over \((u,v)\in R^2\), and apply character orthogonality \(\sum_{u\in R}\exp(2\pi i u t/N)=N\mathbf1_{t=0}\) in each coordinate. The surviving ordered quadruples are precisely those counted by \(\sum_{s,z}r(s,z)^2\), giving \(N^2E(H)\). Division by \(m^4\) yields the normalized constant-input fourth moment displayed above. Every step is exact for all allowed \(p,k\).

## Verification

Run `python3 verify.py` using only the Python standard library. It independently enumerates every ordered pair and all \(N^2\) sum targets for seven prime-power rings \((p,k)=(3,2),(3,3),(3,4),(5,2),(5,3),(7,2),(11,2)\); compares the complete positive and zero fiber histograms; checks the exact energy formula; and directly evaluates the complex two-parameter Fourier fourth moment for moduli \(9\) and \(25\). These computations check \(437\) rows and \(27,540\) ordered pairs. Output ends `VERIFY_OK fields=7 rows=437 ordered_pairs=27540 direct_moments=2`. This is finite corroboration; the proof above supplies the unrestricted conclusion.

## Relationship to prior work

Shparlinski's survey [1] provides modular-hyperbola and Kloosterman context. Bower–Evans–Luo–Miller [2] evaluate **coordinate sumsets** \(\{x+x^{-1}:x\in U\}\) and related variants: they do not count sums of **two hyperbola points** as ordered pairs in \(R^2\). Khan–Magner–Senger–Winterhof [3] study Euclidean lines and distances of modular-hyperbola points, rather than the pair-sum convolution. Guo–Geng–Pan [4] and Gong–Veys–Wan [5] investigate moments of one-variable families of Kloosterman sums (including twisted variants); neither formulation specifies the two-variable pair-sum fiber distribution. The unit-coefficient one-variable moment in [5], even where it can be used to recompute a portion of the aggregate fourth moment, does not recover the full individual \(r(s,z)\) census, particularly the nilpotent-sum rows. The contribution assessed here is the **entire valuation-stratified representation spectrum**, with the full two-parameter moment as a consequence, not a claim to invent Hensel's lemma or Fourier orthogonality.

## Limitations

This theorem is restricted to odd prime powers of exponent at least two and the unweighted modular hyperbola. It does not establish the sharp fourth-power extension constant over arbitrary coefficient functions, or any general characterization for even moduli. The nearest prior number-theoretic sources sometimes use related quadratic-congruence techniques; possible exact reformulations in additional historical Kloosterman-moment literature cannot be ruled out without independent priority review. A 2011 paper by Zhang on classical Kloosterman fourth moments and a 2016 paper on general twisted Kloosterman fourth moments could not be inspected fully; their known abstracts and accessible introductions concern different averaging regimes. No independent mathematical audit has been performed.

## References

1. I. E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879, first public 2011-03-15. https://arxiv.org/abs/1103.2879.
2. A. Bower, R. Evans, V. Luo, S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930v1 (2012). https://arxiv.org/html/1212.2930v1.
3. M. R. Khan, R. Magner, S. Senger, A. Winterhof, *Two Combinatorial Geometric Problems Involving Modular Hyperbolas*, arXiv:1304.6943v1 (2013). https://arxiv.org/abs/1304.6943.
4. X. Guo, G. Geng, X. Pan, *On the fourth power mean of the general kth Kloosterman sums*, SpringerPlus 2014, DOI 10.1186/1687-1847-2014-103.
5. K. Gong, W. Veys, D. Wan, *Power moments of Kloosterman sums*, J. Number Theory 2016, freely available full-text manuscript https://lirias.kuleuven.be/retrieve/23ae295e-1e5b-4b38-9eb6-d038e8c14ee1.
6. W. Zhang, *On the fourth power mean of the general Kloosterman sums*, J. Number Theory 169 (2016), DOI 10.1016/j.jnt.2016.05.018.
7. W. Zhang, *The fourth and sixth power mean of classical Kloosterman sums*, J. Number Theory (2011), DOI 10.1016/j.jnt.2010.08.008.
