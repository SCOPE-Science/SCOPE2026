# Sharp prime-power-base valuations for highly colored digital partitions

## Finding
Let \(p\) be prime, let \(a\ge2\) and \(k=p^a\), and let \(m\ge1\). In the colored \(k\)-ary partition family of Ulas and Żmija, define
\[
H_{k,m}(x)=(1-x)^{-m}\prod_{j\ge0}(1-x^{k^j})^{-m(k-1)}
=\sum_{n\ge0}S_{k,m}(n)x^n.
\]
Write \(s=\nu_p(m)\). Suppose either \(p=2\) and \(s\ge a\), or \(p\) is odd and \(s\ge a-1\). For every \(n\ge1\), put \(t=\nu_p(n)\), \(r=t\bmod a\in\{0,\ldots,a-1\}\), and \(u=n/p^t\) (so \(p\nmid u\)). Then
\[
\boxed{\nu_p(S_{p^a,m}(n))=s+a-r}
\quad\text{and}\quad
\boxed{\frac{S_{p^a,m}(n)}{p^{s+a-r}}\equiv\frac{m}{p^s}u^{-1}\pmod p.}
\]
The quotient in the second formula is an integer, and its residue is nonzero. For \(n=0\), separately, \(S_{k,m}(0)=1\). These formulas give all valuation levels, their exact occurrence criterion, and their first nonzero \(p\)-adic digits.

For fixed \(p,a,m\) as above, the sequence indexed by \(n\ge1\) is \(p\)-automatic: it depends only on the number of trailing zero digits of the base-\(p\) expansion modulo \(a\). The level indexed by \(r\) has natural density
\[
\delta_r=\frac{(1-p^{-1})p^{-r}}{1-p^{-a}}\qquad (0\le r<a).
\]

In the first composite-base case \(p=2,a=2\), and for every integer \(s\ge2\),
\[
\nu_2(S_{4,2^s}(n))=s+2-(\nu_2(n)\bmod2)
=s+1+(\nu_2(2n)\bmod2),\quad n\ge1.
\]
This is precisely Conjecture 6.6(5) of Ulas--Żmija. For every integer \(s\ge3\) and nonnegative integer \(w\), \(2^sw+2^{s-1}\) has \(2\)-adic valuation \(s-1\); the same theorem gives identical \(2\)-adic valuations, hence identical \(4\)-adic valuations, for \(S_{4,2^sw+2^{s-1}}(n)\) and \(S_{4,2^{s-1}}(n)\), proving their Conjecture 6.6(6) for \(n\ge1\).

## Assumptions and scope
The indeterminate \(x\) is formal. Products are interpreted in \(\mathbb Z[[x]]\); each coefficient depends on finitely many factors. The valuation \(\nu_p\) is the ordinary exponent of \(p\) in a nonzero integer. A positive integer \(m\) is assumed, so the coefficients count colored partitions. All congruences concerning normalized integers are taken in \(\mathbb Z/p\mathbb Z\). The theorem covers arbitrary prime powers \(p^a\) with \(a\ge2\) and sufficiently divisible color parameter \(m\); it does not assert anything for smaller \(\nu_p(m)\).

## Proof
**1. Exact logarithmic coefficient.** Put
\[
G_k(x)=H_{k,1}(x)=(1-x)^{-1}\prod_{j\ge0}(1-x^{k^j})^{-(k-1)}.
\]
In \(\mathbb Q[[x]]\), the identity \(-\log(1-z)=\sum_{h\ge1}z^h/h\) gives, for every \(n\ge1\),
\[
[x^n]\log G_k(x)
=\frac{1+(k-1)\sum_{j=0}^{v_k(n)}k^j}{n}
=\frac{k^{v_k(n)+1}}{n},
\]
where \(v_k(n)=\max\{j\ge0:k^j\mid n\}\). The second equality is an exact geometric-sum identity; it does not require \(k\) prime.

Set \(k=p^a\), \(t=\nu_p(n)=aq+r\) with \(0\le r<a\), and \(n=p^tu\), \(p\nmid u\). Since \(v_k(n)=q\), we have the exact rational identity
\[
[x^n]\log G_{p^a}(x)=\frac{p^{a(q+1)}}{p^{aq+r}u}
=\frac{p^{a-r}}{u}.
\]
Thus \(L(x)=\log G_{p^a}(x)\) belongs to \(p\,x\mathbb Z_p[[x]]\), and its \(n\)-th coefficient has valuation exactly \(a-r\).

**2. Uniform suppression of nonlinear exponential terms.** Write \(m=p^sv\) with \(p\nmid v\), and \(A(x)=mL(x)\). Then \(A(x)\in p^{s+1}x\mathbb Z_p[[x]]\), and
\[
H_{p^a,m}(x)=\exp(A(x))
=1+A(x)+\sum_{j\ge2}\frac{A(x)^j}{j!}.
\]
Every coefficient of the summand with index \(j\) has \(p\)-adic valuation at least \(j(s+1)-\nu_p(j!)\).

If \(p=2\), Legendre's bound \(\nu_2(j!)\le j-1\) gives, for \(j\ge2\),
\[
j(s+1)-\nu_2(j!)\ge js+1\ge2s+1\ge s+a+1
\]
under \(s\ge a\). If \(p\) is odd, Legendre's bound \(\nu_p(j!)\le(j-1)/2\) gives
\[
j(s+1)-\nu_p(j!)\ge j(s+1/2)+1/2\ge 2s+3/2.
\]
Since the left-hand side is an integer, it is at least \(2s+2\ge s+a+1\) under \(s\ge a-1\). For each fixed coefficient only finitely many exponential summands contribute, because \(A(0)=0\). Therefore, in all allowed cases,
\[
H_{p^a,m}(x)\equiv1+A(x)\pmod{p^{s+a+1}}
\]
coefficientwise in \(\mathbb Z_p[[x]]\).

**3. Exact valuation and leading unit.** For every \(n\ge1\), Step 1 gives
\[
[x^n]A(x)=m\frac{p^{a-r}}{u}=p^{s+a-r}v u^{-1}.
\]
Its valuation is exactly \(s+a-r\le s+a\), while Step 2 shows that all remaining terms have strictly greater valuation. Thus \(S_{p^a,m}(n)\) has valuation \(s+a-r\), and division by this power of \(p\), followed by reduction modulo \(p\), gives the stated nonzero leading digit. The coefficients of \(H_{p^a,m}\) are integers by the product definition, so the normalized quotient is integral.

**4. Automaticity, density, and conjectural specializations.** Scanning a base-\(p\) numeral from its least significant end, the residue of its trailing-zero count modulo \(a\) is recognized by a finite automaton; equivalently, a finite automaton scanning from the other end can update a counter modulo \(a\) on zeros and reset it on nonzero digits. For \(n\ge1\), \(\nu_p(n)=r+aj\) has asymptotic frequency \((1-p^{-1})p^{-r-aj}\) for each \(j\ge0\). Summing the geometric series yields \(\delta_r\). The two \(k=4\) specializations stated above then follow directly. This completes the proof.

## Verification
The standalone standard-library program `verify.py` reconstructs the exact integer functional equation
\[
(1-x)^{km}H_{k,m}(x)=(1-x^k)^mH_{k,m}(x^k),
\]
uses its coefficient recurrence modulo a sufficiently high power of \(p\), and verifies both the valuations and leading-unit congruences on 12,900 positive indices across eight parameter configurations. Independently, it checks the geometric logarithm coefficient formula at 7,000 arguments and the relevant Legendre inequalities for small indices. Run `python3 verify.py`; success prints `VERIFY_OK`. Finite checks are corroboration only, not the proof of the infinite statement.

## Relationship to prior work
Ulas and Żmija, *On \(p\)-adic valuations of certain \(m\) colored \(p\)-ary partition functions* (first public arXiv posting 6 April 2019; journal version 2020/2021), introduce the identical generating function, prove precise valuations when the base is prime, and state the two particular \(k=4\) formulas as Conjecture 6.6(5) and Conjecture 6.6(6). Their Problem 6.7 asks for \(p\)-automaticity in prime-power bases. The present result proves both specified conjectures and settles a nontrivial high-divisibility range of that problem. It does **not** claim to solve the full problem for arbitrary \(m\), or to reprove the already established prime-base results as novel.

The earlier Ulas--Żmija paper on uniformly colored \(p\)-ary partitions concerns a different product; later work by Żmija on *Arithmetic properties of colored \(p\)-ary partitions* (2023) concerns all \(p\)-power part sizes with a uniform number of colors, possibly finitely many exceptional colors. Its accessible abstract is not a full-text exclusion check; potential stronger coverage remains a bibliographic risk. Targeted mathematical-record searches have not located an exact prior statement of the present prime-power-base formula.

## Limitations
The conditions on \(s\) are sufficient, not asserted necessary. The proof does not characterize the remaining small-color parameters, address bases with two or more distinct prime factors, or determine higher normalized \(p\)-adic digits. Although the two original conjectured formulas are verified by an exact proof, publication priority is subject to an unindexed or inaccessible stronger theorem. The 2023 relevant full text was unavailable for complete inspection. No independent scientific audit has been performed.

## References
1. M. Ulas and B. Żmija, *On p-adic valuations of certain m colored p-ary partition functions*, arXiv:1904.03398 (first posted 2019-04-06), *Ramanujan Journal* 55 (2021), 623–660, DOI: 10.1007/s11139-020-00256-z. Source of the definition, prime-base results, Conjecture 6.6(5)–(6), and Problem 6.7.
2. M. Ulas and B. Żmija, *On p-adic valuations of colored p-ary partitions*, *Monatshefte für Mathematik* 188 (2019), 351–368, DOI: 10.1007/s00605-018-1227-2. Different uniform-color generating function.
3. B. Żmija, *Arithmetic properties of colored p-ary partitions*, *Acta Mathematica Hungarica* 171 (2023), 53–66, DOI: 10.1007/s10474-023-01382-y. Relevant comparison, abstract available; full text not inspected.
