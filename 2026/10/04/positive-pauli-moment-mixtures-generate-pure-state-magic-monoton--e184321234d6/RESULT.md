# Positive Pauli-moment mixtures generate pure-state magic monotones
## Finding
Let \(d_n=2^n\), let \(\mathcal P_n\) denote the phase-free \(n\)-qubit Pauli operators, and for a pure state \(\psi\) set
\[
P_m(\psi)=\frac{1}{d_n}\sum_{P\in\mathcal P_n}|\langle\psi|P|\psi\rangle|^{2m},\qquad m=1,2,\ldots .
\]
Let \(c=(c_m)_{m\ge1}\) be any nonnegative summable sequence satisfying
\[
C:=\sum_{m\ge1}c_m\in(0,\infty),
\]
and suppose \(c_m>0\) for at least one integer \(m\ge2\). Define
\[
G_c(\psi)=\sum_{m\ge1}c_mP_m(\psi),
\qquad
M_c(\psi)=\log_2\!\left(\frac{C}{G_c(\psi)}\right).
\]
Then \(M_c\) is a faithful pure-state magic monotone under deterministic pure-state stabilizer protocols. Precisely, whenever such a protocol maps a pure state \(\psi\) to a pure state \(\phi\),
\[
M_c(\psi)\ge M_c(\phi).
\]
Moreover,
\[
M_c(\psi)=0
\quad\Longleftrightarrow\quad
\psi\text{ is a pure stabilizer state}.
\]

For the particular coefficients
\[
c_m=\frac{\beta^{2m}}{(2m)!},\qquad \beta\in\mathbb R\setminus\{0\},
\]
one has \(C=\cosh(\beta)-1\), and the resulting \(M_c\) is exactly the finite-temperature stabilizer work defined in Salazar--Saxena--Baker--Kwek--Kyaw. Thus the stabilizer-work monotonicity asserted there follows for their deterministic pure-state stabilizer protocol class.

## Assumptions and scope
The theorem concerns finite-qubit pure states and deterministic stabilizer protocols whose input and output remain pure. The allowed operations are the standard pure-state stabilizer operations: Clifford unitaries, adjoining pure stabilizer ancillas, computational-basis measurements when the overall deterministic protocol has a pure output, and pure-state-preserving discarding as covered by the deterministic protocol notion used in the cited stabilizer-entropy theorem.

The coefficient sequence is required to be nonnegative and summable. At least one coefficient with index \(m\ge2\) must be positive for faithfulness. The case with only \(c_1>0\) is excluded because \(P_1(\psi)=1\) for every pure state. No statement is made for mixed-state protocols, arbitrary stabilizer-preserving maps, or strong/average monotonicity over individual measurement branches.

## Proof
For a pure \(n\)-qubit state, Pauli Parseval gives
\[
\sum_{P\in\mathcal P_n}|\langle\psi|P|\psi\rangle|^2=d_n,
\]
so \(P_1(\psi)=1\).

For every integer \(m\ge2\), Leone and Bittel proved that the stabilizer Rényi entropy
\[
\mathcal M_m(\psi)=\frac{1}{1-m}\log_2 P_m(\psi)
\]
is monotone under every deterministic pure-state stabilizer protocol. Thus, if \(\psi\mapsto\phi\),
\[
\mathcal M_m(\psi)\ge\mathcal M_m(\phi).
\]
Because \(1-m<0\), this is equivalent to
\[
P_m(\psi)\le P_m(\phi),\qquad m\ge2.
\]
Together with \(P_1(\psi)=P_1(\phi)=1\) and \(c_m\ge0\), termwise comparison yields
\[
G_c(\psi)\le G_c(\phi).
\]
The series is absolutely convergent because \(0<P_m(\psi)\le1\) and \(\sum_m c_m<\infty\). Since the logarithm is increasing,
\[
M_c(\psi)=\log_2\!\left(\frac{C}{G_c(\psi)}\right)
\ge
\log_2\!\left(\frac{C}{G_c(\phi)}\right)
=M_c(\phi).
\]

Faithfulness follows from the same moment structure. Since every Pauli expectation has modulus at most one,
\[
P_m(\psi)\le P_1(\psi)=1
\]
for every \(m\ge2\), hence \(G_c(\psi)\le C\) and \(M_c(\psi)\ge0\). A pure stabilizer state has exactly \(d_n\) phase-free Pauli expectations of modulus one and all remaining expectations zero, so \(P_m=1\) for every \(m\), giving \(M_c=0\).

Conversely, suppose \(M_c(\psi)=0\). Then
\[
0=C-G_c(\psi)=\sum_{m\ge1}c_m\bigl(1-P_m(\psi)\bigr).
\]
Every summand is nonnegative, and some \(c_r>0\) with \(r\ge2\), so \(P_r(\psi)=1\). Subtracting the normalized second-moment identity gives
\[
0=P_1(\psi)-P_r(\psi)
=\frac{1}{d_n}\sum_{P\in\mathcal P_n}
\left(|\langle P\rangle_\psi|^2-|\langle P\rangle_\psi|^{2r}\right).
\]
Each term is nonnegative, hence every Pauli expectation has modulus either zero or one. Parseval then forces exactly \(d_n\) phase-free Paulis to have modulus one. After choosing the sign that makes each such Hermitian Pauli fix \(\psi\), these operators commute, are closed under multiplication, and form an Abelian stabilizer group of size \(d_n\). Its joint \(+1\) eigenspace is one-dimensional, so \(\psi\) is a pure stabilizer state.

Finally, for real \(\beta\ne0\), expand
\[
\cosh(\beta x)-1
=\sum_{m\ge1}\frac{\beta^{2m}x^{2m}}{(2m)!}.
\]
With \(c_m=\beta^{2m}/(2m)!\), the core stabilizer partition function of Salazar--Saxena--Baker--Kwek--Kyaw is
\[
Z_\beta^c(\psi)
=e^{-\beta}d_nG_c(\psi),
\]
whereas a pure stabilizer reference has
\[
Z_\beta^c(\mathrm{STAB}_n)
=e^{-\beta}d_nC.
\]
Therefore their stabilizer work is
\[
-\log_2 Z_\beta^c(\psi)+\log_2 Z_\beta^c(\mathrm{STAB}_n)
=M_c(\psi),
\]
which proves the stated corollary.

## Verification
The proof uses no finite enumeration or numerical extrapolation. The critical imported theorem was checked in the full text of Leone--Bittel: for every integer order at least two, their Theorem 1 gives monotonicity of the stabilizer Rényi entropy under deterministic pure-state stabilizer protocols. The sign reversal from entropy monotonicity to \(P_m(\psi)\le P_m(\phi)\) was checked explicitly using \(1-m<0\).

The finite-temperature identification was checked directly against the defining core partition function and stabilizer-work normalization in Salazar--Saxena--Baker--Kwek--Kyaw. Dimension factors cancel between the state and the stabilizer reference, so the formula remains valid when a deterministic protocol changes the number of qubits.

## Relationship to prior work
Leone and Bittel proved monotonicity separately for every integer-order stabilizer Rényi entropy, equivalently for each normalized stabilizer purity \(P_m\). They did not state the nonnegative summable-mixture closure above. Their paper also distinguishes ordinary deterministic monotonicity from strong measurement-branch monotonicity.

Salazar, Saxena, Baker, Kwek, and Kyaw introduced the core stabilizer partition function and the associated finite-temperature stabilizer work. Their paper states stabilizer work as a faithful monotone and uses its monotonicity in a one-shot interconversion bound. The inspected full text does not supply a theorem proving that finite-temperature monotonicity for the measurement-containing deterministic pure-state protocol class. The present theorem is broader than that individual finite-temperature functional: it gives an infinite cone of faithful monotones generated by arbitrary nonnegative summable mixtures of all integer Pauli moments, with stabilizer work as one analytic coefficient choice.

Bittel and Leone later gave operational interpretations and testing results for stabilizer Rényi quantities. The inspected material does not state the positive-mixture closure theorem above.

## Limitations
The theorem does not prove strong monotonicity averaged over arbitrary measurement branches. In fact, the cited stabilizer-entropy literature warns that the logarithmic stabilizer Rényi entropies themselves are not generally strong monotones. The theorem also does not address mixed states, arbitrary stabilizer-preserving channels, negative mixture coefficients, nonsummable coefficient sequences, or the singular value \(\beta=0\) in the partition-function ratio. No claim is made that every pure-state magic monotone has the displayed form.

## References
1. W. E. Salazar, G. Saxena, J. S. Baker, L. C. Kwek, and T. H. Kyaw, “Stabilizer Statistical Mechanics: A Framework for Efficient Quantification and Classification of Magic States,” arXiv:2608.14798. Public conference abstract: LPHYS'26 talk 4023, 10 July 2026.
2. L. Leone and L. Bittel, “Stabilizer entropies are monotones for magic-state resource theory,” Physical Review A 110, L040403 (2024), doi:10.1103/PhysRevA.110.L040403, arXiv:2404.11652.
3. L. Bittel and L. Leone, “Operational interpretation of the Stabilizer Entropy,” Quantum 10, 2069 (2026), doi:10.22331/q-2026-04-15-2069, arXiv:2507.22883.
