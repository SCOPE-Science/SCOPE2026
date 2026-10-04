# Exact generic-stratum discontinuity interval of two-sided measurement-induced nonlocality at Werner states

## Finding

For \(m\ge2\), consider the Werner state
\[
\rho_x
=
\frac{m-x}{m^3-m}I
+
\frac{mx-1}{m^3-m}F,
\qquad
x\in[0,1],
\]
on \(\mathbb C^m\otimes\mathbb C^m\), where \(F\) is the flip operator. Write
\[
b=\frac{mx-1}{m^3-m}.
\]
For the two-sided Hilbert--Schmidt measurement-induced nonlocality
\[
N_{AB}(\rho)
=
\max_{\Pi^{ab}}
\|\rho-\Pi^{ab}(\rho)\|_2^2,
\]
the maximization is over rank-one local projective measurements leaving both marginals invariant.

Guo proved that this quantity is not continuous and used Werner states to exhibit the phenomenon. The exact local geometry at every Werner state is as follows.

Among all sequences \(\tau_r\to\rho_x\) in trace norm such that both marginals of every \(\tau_r\) are nondegenerate, the complete set of subsequential limits of \(N_{AB}(\tau_r)\) is
\[
\boxed{
\left[
 b^2(m^2-m),
 b^2(m^2-1)
\right].
}
\]
Since
\[
N_{AB}(\rho_x)=b^2(m^2-1),
\]
this is equivalently
\[
\boxed{
\left[
\frac{m}{m+1}N_{AB}(\rho_x),
N_{AB}(\rho_x)
\right].
}
\]
Thus, whenever \(x\ne1/m\), the exact local oscillation width contributed by the generic nondegenerate-marginal stratum is
\[
\boxed{
\frac{1}{m+1}N_{AB}(\rho_x).
}
\]
At \(x=1/m\), the Werner state is maximally mixed and this interval collapses to \(\{0\}\).

More precisely, suppose the unique eigenbases of the two nondegenerate marginals converge to bases whose overlap matrix is a unitary \(U\). Then
\[
N_{AB}(\tau_r)
\longrightarrow
b^2\left[m^2-S(U)\right],
\qquad
S(U)=\sum_{i,j=1}^m |U_{ij}|^4.
\]
The lower endpoint occurs for aligned bases, while the upper endpoint occurs for mutually unbiased bases.

## Assumptions and scope

The state family and the two-sided Hilbert--Schmidt MiN are exactly those of Guo's arXiv construction. The result concerns finite dimension \(m\ge2\).

The approaching states are required to have both reduced density matrices nondegenerate. This is the natural generic stratum because then the locally invariant rank-one projective measurement is uniquely determined by the two marginal eigenbases.

No claim is made here about trace-norm MiN, fidelity-based MiN, relative-entropy MiN, or other modified correlation measures. Those quantities were introduced partly to avoid pathologies of Hilbert--Schmidt constructions and have different optimization geometry.

## Proof

Fix orthonormal bases \(\{|a_i\rangle}\}\) and \(\{|b_j\rangle}\}\) of the two factors and let
\[
U_{ij}=\langle a_i|b_j\rangle.
\]
Let \(\Pi_U\) be dephasing in the product basis \(\{|a_i\rangle\otimes|b_j\rangle}\}\).

Because \(\Pi_U\) is the Hilbert--Schmidt orthogonal projection onto the diagonal algebra and
\[
\langle a_i b_j|F|a_i b_j\rangle
=
|U_{ij}|^2,
\]
one has
\[
\Pi_U(F)
=
\sum_{i,j}|U_{ij}|^2
|a_i b_j\rangle\langle a_i b_j|.
\]
Hence
\[
\|\Pi_U(F)\|_2^2
=
\sum_{i,j}|U_{ij}|^4
=S(U),
\]
whereas \(\|F\|_2^2=m^2\). Orthogonality of the dephasing projection gives
\[
\|F-\Pi_U(F)\|_2^2
=m^2-S(U).
\]
Since the identity part of \(\rho_x\) is unchanged by dephasing,
\[
\|\rho_x-\Pi_U(\rho_x)\|_2^2
=b^2[m^2-S(U)].
\]

For each row of a unitary matrix, the numbers \(|U_{ij}|^2\) form a probability vector. Therefore
\[
\frac1m
\le
\sum_j |U_{ij}|^4
\le
1,
\]
and summing over rows yields
\[
1\le S(U)\le m.
\]
The value \(m\) is attained by a permutation unitary, corresponding to aligned bases. The value \(1\) is attained by any complex Hadamard matrix, for example the discrete Fourier matrix, corresponding to mutually unbiased bases. Since \(U(m)\) is connected and \(S\) is continuous, its image is the whole interval \([1,m]\).

At the Werner state both marginals are maximally mixed, so every product basis is admissible. Maximizing the disturbance therefore means minimizing \(S(U)\), and hence
\[
N_{AB}(\rho_x)
=b^2(m^2-1).
\]

Now let \(\tau_r\to\rho_x\) in trace norm and suppose both marginals of every \(\tau_r\) are nondegenerate. The invariant two-sided projective measurement is then uniquely the product of the two marginal eigenbases. Any sequence of such bases has a convergent subsequence in the compact flag manifolds, after harmless phase and permutation choices. Along that subsequence the corresponding dephasing maps converge, while trace-norm convergence implies Hilbert--Schmidt convergence in finite dimension. Consequently every subsequential limit of \(N_{AB}(\tau_r)\) has the form
\[
b^2[m^2-S(U)]
\]
for some unitary \(U\), and therefore lies in the asserted interval.

Conversely, fix any unitary \(U\). Choose density matrices \(\sigma_A\) and \(\sigma_B\) with pairwise distinct eigenvalues in bases whose overlap is \(U\), and put
\[
\sigma=\sigma_A\otimes\sigma_B,
\qquad
\tau_\varepsilon
=
\frac{\rho_x+\varepsilon\sigma}{1+\varepsilon},
\qquad
\varepsilon>0.
\]
Both marginals of \(\tau_\varepsilon\) are nondegenerate and have exactly those chosen eigenbases. Moreover \(\Pi_U(\sigma)=\sigma\), so
\[
N_{AB}(\tau_\varepsilon)
=
\frac{b^2[m^2-S(U)]}{(1+\varepsilon)^2}.
\]
Letting \(\varepsilon\downarrow0\) realizes the desired limit. Because every value of \(S(U)\) in \([1,m]\) occurs, the cluster set is exactly the full interval claimed.

Finally,
\[
\frac{m^2-m}{m^2-1}
=
\frac{m}{m+1},
\]
which gives the normalized interval and exact oscillation width.

## Verification

The accompanying script `verify_werner_cluster.py` reconstructs the flip operator, product dephasing maps, Fourier and aligned bases, and explicit nondegenerate product perturbations. It checks the disturbance identity, the endpoint formulas, the exact perturbation scaling, and intermediate overlap values in dimensions \(2\) through \(6\).

The finite replay is supplementary. Completeness of the interval is analytic and follows from compactness of limiting eigenbases, the connectedness of \(U(m)\), and the exact dephasing formula above.

## Relationship to prior work

Guo introduced two-sided measurement-induced nonlocality, proved its noncontinuity, and used precisely the Werner family with aligned and mutually unbiased perturbing marginal bases to demonstrate that different approaches can have different limiting disturbances. That qualitative discontinuity and the choice of endpoint-type bases are prior work.

The finding here is narrower and quantitative: it computes the exact disturbance for an arbitrary relative limiting basis, proves that the fourth-power overlap functional fills the entire interval \([1,m]\), and proves that no other limit can occur when the approaching states have nondegenerate marginals. This yields the complete generic-stratum cluster set and the universal relative oscillation factor \(1/(m+1)\).

Later work replacing the Hilbert--Schmidt norm by trace, fidelity, affinity, or related distances addresses different correlation measures and does not supply this local cluster-set classification for Guo's original two-sided Hilbert--Schmidt quantity. Targeted searches for a quantitative Werner-state discontinuity interval, mutually-unbiased-basis endpoint formula, and nondegenerate-marginal cluster set did not locate an equivalent statement.

## Limitations

The classification concerns approach through states whose two marginals are both nondegenerate. Approaches that remain on degenerate strata can retain extra measurement freedom and are not classified here.

The result is specific to Werner states and the squared Hilbert--Schmidt version of two-sided MiN. It does not assert analogous intervals for other state families or norm-based variants.

A residual literature risk remains because a general stratified-optimization treatment of degenerate quantum-correlation measures could imply the interval abstractly without using Werner-state notation.

## References

1. Y. Guo, “Measurement-induced nonlocality over two-sided projective measurements,” arXiv:1204.0565, first submitted 3 April 2012; *International Journal of Modern Physics B* 27 (2013), 1350067, DOI: 10.1142/S0217979213500677.
2. S. Luo and S. Fu, “Measurement-induced nonlocality,” *Physical Review Letters* 106 (2011), 120401, DOI: 10.1103/PhysRevLett.106.120401.
3. M.-L. Hu and H. Fan, “Measurement-induced nonlocality based on the trace norm,” arXiv:1402.4321; *New Journal of Physics* 17 (2015), 033004.
4. R. Muthuganesan and R. Sankaranarayanan, “Fidelity based Measurement Induced Nonlocality over two-sided measurements,” arXiv:1802.05660; *International Journal of Quantum Information* 16 (2018), 1850054.
