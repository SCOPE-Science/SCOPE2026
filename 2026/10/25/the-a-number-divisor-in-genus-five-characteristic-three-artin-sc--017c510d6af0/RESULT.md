# The a-number divisor in genus-five characteristic-three Artin–Schreier moduli

## Finding

Let \(k\) be algebraically closed of characteristic \(3\), and let \(C\) be a smooth projective connected genus-five Artin–Schreier cover of \(\mathbb P^1_k\). Its ramification jumps are either \((4,1)\) or \((2,1,1)\). In the former case the cover can be written, up to an Artin–Schreier change of variables and a projective change of its base coordinate, as
\[
y^3-y=x^4+a x^2+b x+c/x,\qquad a,b\in k,\quad c\in k^\times.
\]
Write \(\mathfrak a(C)\) for the Jacobian's a-number. Then
\[
\mathfrak a(C)=\begin{cases}2,&a\ne0,\\3,&a=0.\end{cases}
\]
In the other ramification stratum \((2,1,1)\), every curve has \(\mathfrak a(C)=1\). Consequently the genus-five Artin–Schreier locus has exactly three nonempty a-number strata: \(\mathfrak a=1\) of dimension \(4\), \(\mathfrak a=2\) of dimension \(3\), and \(\mathfrak a=3\) of dimension \(2\). On the normalized two-pole parameter space the rank-jump locus is the reduced divisor \(a=0\).

## Assumptions and scope

All dimensions refer to the loci of isomorphism classes of Artin–Schreier covers over an algebraically closed field, with finite fibers to the corresponding smooth genus-five curve locus. An Artin–Schreier cover means a nontrivial cyclic degree-three map from a smooth projective connected curve to \(\mathbb P^1_k\). The \(a\)-number \(\mathfrak a(C)\) is the dimension of the kernel of the Cartier operator on \(H^0(C,\Omega^1_C)\), equivalently the a-number of the Jacobian. The coefficient \(a\) is distinct from this intrinsic invariant.

## Proof

**Ramification and normal form.** For pole orders \(m_i\) prime to \(3\), set \(e_i=m_i+1\). Riemann–Hurwitz yields \(g=\sum_i e_i-2\) in characteristic three. Thus genus five gives \(\sum_i e_i=7\), with \(e_i\ge2\) and \(e_i\not\equiv1\pmod3\). The only partitions are \((5,2)\) and \((3,2,2)\), corresponding respectively to jumps \((4,1)\) and \((2,1,1)\). Deuring–Shafarevich gives p-rank \(2\) in the former case and \(4\) in the latter.

For jumps \((4,1)\), move the respective branch points to infinity and zero. Remove terms whose exponents are divisible by three using \(y\mapsto y+h(x)\), remove a constant by translating \(y\), and scale \(x\) to make the coefficient of \(x^4\) equal to one. This gives the displayed normal form with \(c\ne0\). The vanishing of the coefficient \(a\) is unchanged by the remaining normalizations (scalings of \(x\), translations of \(y\) and Artin–Schreier representatives).

**Five regular differentials.** Let \(P_\infty\) and \(P_0\) be the unique points above the two poles. The local Artin–Schreier valuations and the different formula give
\[
\begin{array}{c|ccc}
&v(x)&v(y)&v(dx)\\\hline
P_\infty&-3&-4&4\\
P_0&3&-1&4
\end{array}
\qquad\text{and}\qquad \operatorname{div}(dx)=4P_\infty+4P_0.
\]
There are no other possible poles. Therefore
\[
\omega_1=dx/x,\quad\omega_2=dx,\quad\omega_3=x\,dx,\quad
\omega_4=y\,dx/x,\quad\omega_5=y\,dx
\]
are everywhere regular. They are linearly independent: the first three multiply \(dx\) by independent rational functions in \(x\), whereas the last two multiply it by \(y\) times independent rational functions in \(x\); and \([k(C):k(x)]=3\). Since \(g=5\), they form a basis of \(H^0(C,\Omega^1_C)\).

**Exact Cartier calculation.** Write \(\mathcal C\) for Cartier, which is \(3^{-1}\)-semilinear. Use
\[
\mathcal C(x^{3j+2}\,dx)=x^j\,dx,\quad
\mathcal C(dx/x)=dx/x,\quad
\mathcal C(h^3\eta)=h\,\mathcal C(\eta),
\]
with coefficients taken to their unique cube roots in \(k\). Substituting \(y^3=y+x^4+a x^2+b x+c/x\) gives, in this order,
\[
\mathcal C(\omega_1)=\omega_1,\qquad
\mathcal C(\omega_2)=\mathcal C(\omega_3)=0,\qquad
\mathcal C(\omega_4)=\omega_4,
\]
\[
\boxed{\mathcal C(\omega_5)=-c^{1/3}\omega_1-a^{1/3}\omega_2.}
\]
Here the term \(b x\,dx\) vanishes under Cartier; \(c\,dx/x\) and \(a x^2\,dx\) are the only surviving contributions from \(f(x)\,dx\). Since \(\mathcal C(\omega_5)\) adds a third independent image exactly when \(a\ne0\), the Cartier rank is respectively \(3\) or \(2\). Its nullity is \(2\) or \(3\), as asserted. The stable Cartier rank is two, consistent with the independent p-rank calculation.

**Other pole type and dimensions.** In the three-pole case the p-rank is four while the genus is five. The general inequality \(1\le\mathfrak a(C)\le g-f\) when \(f<g\) forces \(\mathfrak a(C)=1\). Pries–Zhu's ramification-partition dimension formula gives \(4\) for \((3,2,2)\) and \(3\) for \((5,2)\). The displayed two-pole normal-form parameter space is \(\mathbb A^2\times\mathbb G_m\), and the condition \(a=0\) cuts out a nonempty irreducible reduced surface. Since genus-five curves have finite automorphism groups and a fixed curve admits only finitely many cyclic degree-three cover structures, the map from this parameter space to moduli has finite fibers; hence the \(\mathfrak a=3\) locus has dimension two. Its complement has dimension three. This exhausts the possible cases.

## Verification

The companion `verify.py` performs exact arithmetic in \(\mathbb F_3\), independently forming the Laurent-series Cartier contributions and the five-by-five matrix for all \(18\) specializations \(a,b\in\mathbb F_3\), \(c\in\mathbb F_3^\times\). It checks rank \(2\) or \(3\) according to \(a\), stable rank \(2\), the allowed ramification partitions, and nonnegative differential valuations. Execute `python3 verify.py`; successful output begins `VERIFY_OK`. These finite checks supplement but do not replace the characteristic-three symbolic proof above.

## Relationship to prior work

Pries–Zhu classify Artin–Schreier p-rank components, pole partitions and dimensions, but do not determine the two coefficient-sensitive Cartier ranks here. Farnell–Pries prove constant a-number under a congruence condition \(p\equiv1\pmod L\), inapplicable to \(p=3\) and pole lcm \(L=4\). Earlier Farnell work has the same constant-rank focus. Booher–Cais provide general a-number bounds for branched Artin–Schreier covers, rather than the exact normalized jump-divisor statement. Subsequent genus-five invariant-ring tabulations include these pole patterns but not their Cartier-kernel classification. The contribution is the explicit intrinsic a-number transition and complete genus-five a-number/dimension table, not the pre-existing genus, p-rank, partition or ambient-dimension formulas.

## Limitations

The statement is about Artin–Schreier covers of the projective line and their underlying curve moduli over an algebraically closed field, not arbitrary genus-five curves or finite-field Frobenius orbit counts. The divisor is asserted to be reduced on the normalized parameter variety; no assertion about the scheme structure of a corresponding substack or coarse moduli subscheme is needed. Specialized older classification results not located in the searches might contain an equivalent formula. The calculation does not classify full Ekedahl–Oort types beyond the a-number.

## References

- S. Farnell and R. Pries, *Families of Artin–Schreier curves with Cartier–Manin matrix of constant rank*, arXiv:1202.4183 (first posted 2012-02-19).
- R. Pries and H. J. Zhu, *The p-rank stratification of Artin–Schreier curves*, Ann. Inst. Fourier 62 (2012), 707–726, doi:10.5802/aif.2692.
- S. Farnell, *Artin–Schreier Curves*, Colorado State University thesis (2010), doi:10.25675/3.019646.
- J. Booher and B. Cais, *a-Numbers of Curves in Artin–Schreier Covers*, Algebra Number Theory 14 (2020), 593–641, arXiv:1807.10313.
- Duque-Rosero et al., *Computing Invariants of Artin–Schreier Curves*, arXiv:2602.22435, genus-five ramification table (context only).
