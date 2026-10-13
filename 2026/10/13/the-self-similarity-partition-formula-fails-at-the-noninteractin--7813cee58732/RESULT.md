# The self-similarity partition formula fails at the noninteracting Ising point

## Finding

Consider the order-two Cayley-tree Ising model of Akın with nearest-neighbor coupling \(J\), prolonged next-nearest-neighbor coupling \(J_p\), external field \(h\), and inverse temperature \(\beta>0\). At the noninteracting point
\[
J=J_p=h=0,
\]
the Hamiltonian vanishes for every spin configuration.

The source defines the finite rooted tree with
\[
|V_n|=2^{n+1}-1
\]
vertices and the root-conditioned partial partition function \(Z_{i_0}^{(n)}\). Therefore the exact count is
\[
\boxed{Z_{i_0}^{(n)}=2^{|V_n|-1}=2^{2^{n+1}-2}}.
\]

The source also introduces
\[
\theta=e^{\beta J/2},\qquad
\phi=e^{\beta J_p/2},\qquad
u=e^{\beta h/2}.
\]
At the noninteracting point, \(\theta=\phi=u=1\). Its displayed local factor in Theorem 1 then equals
\[
8^2+8^2=128.
\]
Hence the printed theorem gives
\[
\boxed{Z_{i_0,\mathrm{src}}^{(n)}=128^{2^{n-1}-1}
=2^{7(2^{n-1}-1)}}.
\]

These expressions are unequal. Already at \(n=2\), where \(|V_2|=7\), the exact root-conditioned partition function is \(2^6=64\), while the printed formula gives \(128\). At \(n=3\), the printed value is \(2^{21}\), while even the unrestricted partition function is only \(2^{15}\).

It follows that the source's free-energy formula also fails at this point. Under its positive-sign convention,
\[
F(\beta,h)=\lim_{n\to\infty}\frac{1}{\beta|V_n|}\log Z_{i_0}^{(n)},
\]
the exact value is
\[
\boxed{F(\beta,0)=\frac{\log 2}{\beta}},
\]
whereas its Theorem 2 gives
\[
\boxed{F_{\mathrm{src}}(\beta,0)=\frac{7\log 2}{4\beta}}.
\]

## Assumptions and scope

The claim concerns exactly the finite-volume partial partition function and free-energy definition printed in DOI:10.3390/axioms11120703 for the order-two Cayley tree. The root spin is held fixed in \(Z_{i_0}^{(n)}\), exactly as in the source definition. The test point \(J=J_p=h=0\) is inside the model's parameter space and is valid for every \(\beta>0\).

The conclusion is limited to the source's partition-function and free-energy formulas and quantities derived from that free energy. The paper's separate fixed-point phase-transition calculation is not assessed here.

## Proof

When \(J=J_p=h=0\), every term in the Hamiltonian is zero, so every admissible configuration has Boltzmann weight one. A binary Ising spin is attached to each of the \(|V_n|\) vertices. Fixing the root spin leaves exactly \(|V_n|-1\) independent binary choices. Thus
\[
Z_{i_0}^{(n)}=2^{|V_n|-1}.
\]
Using the source's own count \(|V_n|=2^{n+1}-1\) gives the exact formula above.

For the printed formula, substituting \(\theta=\phi=u=1\) into the two squared brackets of Theorem 1 gives
\[
(2+4+2)^2=64
\]
for each bracket, so their sum is \(128\). The exponent in that theorem is \(2^{n-1}-1\), proving the printed expression
\[
128^{2^{n-1}-1}.
\]
Comparison with the exact state count proves Theorem 1 cannot hold as stated.

For the thermodynamic limit,
\[
\frac{1}{\beta|V_n|}\log Z_{i_0}^{(n)}
=
\frac{|V_n|-1}{|V_n|}\frac{\log2}{\beta}
\longrightarrow
\frac{\log2}{\beta}.
\]
Meanwhile, Theorem 2 evaluates at \(\theta=\phi=u=1\) to
\[
\frac{1}{4\beta}\log(128)
=
\frac{7\log2}{4\beta}.
\]
The two limits differ.

The source's derivation identifies a local quantity by summing over \(i_0,i_1,i_2\), hence including both values of the root spin, and then reuses that quantity in a formula labeled as the root-conditioned \(Z_{i_0}^{(n)}\). The noninteracting state count exposes this mismatch without any approximation.

## Verification

The accompanying script `verification/verify.py` checks the exact finite-volume counts for several shells, evaluates the printed expression at \(\theta=\phi=u=1\), and verifies the two free-energy coefficients symbolically as rational multiples of \(\log2/\beta\). These computations replay identities already proved above; they are not substitutes for the proof.

## Relationship to prior work

Akın's 2022 Axioms article states Theorem 1 as an exact finite-volume partition formula and Theorem 2 as the resulting exact free-energy formula. The article's XML gives primary MSC 82B05 and explicitly defines \(\theta=e^{\beta J/2}\), \(\phi=e^{\beta J_p/2}\), and \(u=e^{\beta h/2}\).

Earlier Cayley-tree free-energy work uses boundary-condition or Gibbs-measure constructions rather than the local factorization challenged here. In particular, Gandolfo--Rakhmatullaev--Rozikov--Ruiz study Ising free energies under several boundary conditions, and Mukhamedov--Akın--Khakimov calculate free energies for translation-invariant Gibbs measures of the Ising--Vannimenus model. Neither inspected source states the erroneous noninteracting count above.

Targeted searches for an erratum, correction, or a previously published observation of the \(J=J_p=h=0\) discrepancy did not locate one. A later same-author paper on thermodynamic quantities for arbitrary-order Cayley trees is highly relevant, but only its bibliographic record and abstract were accessible in this check; it is retained as a residual originality risk rather than treated as negative evidence.

## Limitations

This is a counterexample to the printed partition and free-energy formulas, not a complete replacement free-energy theory for nonzero interactions. It does not establish which later formulas in the paper remain valid independently of Theorems 1 and 2. In particular, no conclusion is drawn here about the fixed-point phase-transition criterion.

A later same-author article on arbitrary-order trees may contain a reformulated method that is not visible from its accessible abstract. That access limitation does not affect the correctness of the counterexample to the 2022 formulas, but it remains an originality risk for whether the same correction has appeared elsewhere.

## References

1. H. Akın, “Calculation of the Free Energy of the Ising Model on a Cayley Tree via the Self-Similarity Method,” *Axioms* 11 (2022), 703, DOI:10.3390/axioms11120703.
2. D. Gandolfo, M. M. Rakhmatullaev, U. A. Rozikov, J. Ruiz, “On free energies of the Ising model on the Cayley tree,” arXiv:1211.6648; *Journal of Statistical Physics* 150 (2013), 1201–1217.
3. F. Mukhamedov, H. Akın, O. Khakimov, “Gibbs measures and free energies of Ising-Vannimenus Model on the Cayley tree,” arXiv:1704.01933; *Journal of Statistical Mechanics* (2017), 053208.
4. H. Akın, “Calculation of some thermodynamic quantities for the Ising model on a \(k\)-th order Cayley tree,” *Physica B* 662 (2023), 414929, DOI:10.1016/j.physb.2023.414929.
