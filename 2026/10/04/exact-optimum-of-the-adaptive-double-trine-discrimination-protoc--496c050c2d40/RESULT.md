# Exact optimum of the adaptive double-trine discrimination protocol

## Finding

Consider the equiprobable double-trine ensemble
\[
\{|s_i\rangle\otimes|s_i\rangle: i=0,1,2\}
\]
and the explicit three-round two-way LOCC protocol introduced by Chitambar and Hsieh. Alice's first measurement has strength
\[
p\in[0,1].
\]
For the branch in which Alice obtains outcome \(0\) and Bob obtains outcome \(+\), the normalized posterior probabilities are
\[
P_0=\frac{1-p}{3},
\qquad
P_1=\frac{(2+\sqrt3)(2+p)}{12},
\qquad
P_2=\frac{(2-\sqrt3)(2+p)}{12}.
\]
The two states retained in the final Helstrom test have squared overlap
\[
c(p)=|\langle s'_0|s'_1\rangle|^2
=\frac{1-p}{2(2+p)}.
\]

By the sixfold symmetry of the protocol, every branch has the same conditional error, so the total error is
\[
E(p)=1-\frac12\left(Q(p)+\sqrt{S(p)}\right),
\]
where
\[
Q(p)=P_0+P_1
=\frac{8+2\sqrt3+(\sqrt3-2)p}{12}
\]
and
\[
S(p)=Q(p)^2-4P_0P_1c(p)
=
\frac{20+8\sqrt3+(4+8\sqrt3)p-(3+4\sqrt3)p^2}{48}.
\]

The unique global minimizer on \([0,1]\) is
\[
\boxed{
p_*=\frac{45-8\sqrt3}{39}
}
=
0.798553680498\ldots .
\]
At this parameter,
\[
\boxed{
E_*=\frac{63-32\sqrt3}{117}
}
=
0.0647382406649\ldots .
\]

The endpoint \(p=1\) reproduces the optimal one-way protocol:
\[
E_{\to}
=
\frac12-\frac{\sqrt3}{4}
=
0.0669872981078\ldots .
\]
Hence the exact error reduction supplied by this explicit feedback protocol is
\[
E_{\to}-E_*
=
\frac{11\sqrt3-18}{468}
=
0.00224905744286\ldots>0.
\]

The source reports the minimum only numerically, as approximately \(6.47\times10^{-2}\). The formulas above give the exact measurement strength, exact minimum error, and exact strict gap to the one-way optimum.

## Assumptions and scope

The result concerns exactly the one-parameter adaptive protocol displayed by Chitambar and Hsieh for the equiprobable double-trine ensemble. Alice uses their first-round Kraus operators, Bob performs their \(\{|+\rangle,|-\rangle\}\) measurement, and Alice finishes with the optimal binary Helstrom test after discarding the least likely remaining candidate.

The parameter range is the source range
\[
0\le p\le1.
\]
No claim is made that this family attains the optimal error among all finite-round LOCC protocols or among unrestricted LOCC. The source proves a separation between two-way and one-way communication; the present result sharpens the explicit witness protocol by solving its scalar optimization exactly.

## Proof

For the representative branch \((A_0,B_+)\), the source gives the conditional event probabilities
\[
P_{A_0B_+|0}=\frac{1-p}{6},
\]
\[
P_{A_0B_+|1}
=
\frac{(2+\sqrt3)(2+p)}{24},
\]
and
\[
P_{A_0B_+|2}
=
\frac{(2-\sqrt3)(2+p)}{24}.
\]
Their sum is \(1/2\), so after incorporating the equiprobable prior and normalizing the branch, the posterior probabilities are twice these quantities. This yields \(P_0,P_1,P_2\) in the finding.

The two states retained by Alice are
\[
|s'_0\rangle=|0\rangle
\]
and
\[
|s'_1\rangle
=
\frac{\sqrt{1-p}|0\rangle-\sqrt{3(1+p)}|1\rangle}
{\sqrt{2(2+p)}}.
\]
Therefore
\[
c(p)=|\langle s'_0|s'_1\rangle|^2
=
\frac{1-p}{2(2+p)}.
\]

If
\[
Q=P_0+P_1,
\]
the error conditioned on this branch is the probability \(P_2\) of the discarded hypothesis plus the binary Helstrom error for the unnormalized weights \(P_0,P_1\):
\[
E(p)
=
1-\frac{Q}{2}
\left(
1+
\sqrt{1-\frac{4P_0P_1}{Q^2}c(p)}
\right).
\]
All six symmetry-related branches occur with equal probability and have the same conditional error, hence this is also the total protocol error. Writing
\[
S=Q^2-4P_0P_1c
\]
gives the displayed \(Q(p)\) and \(S(p)\) by direct simplification.

Set
\[
H(p)=Q(p)+\sqrt{S(p)}.
\]
Minimizing \(E\) is equivalent to maximizing \(H\). Since
\[
Q'(p)=\frac{\sqrt3-2}{12},
\]
an interior stationary point satisfies
\[
S'(p)=-2Q'(p)\sqrt{S(p)}.
\]
Squaring this necessary equation gives the exact factorization
\[
(S'(p))^2-4(Q'(p))^2S(p)
=
\frac{(p-1)\bigl((18+11\sqrt3)p-(14+9\sqrt3)\bigr)}{216}.
\]
Thus the only candidates in \([0,1]\) are \(p=1\) and
\[
p_*=
\frac{14+9\sqrt3}{18+11\sqrt3}
=
\frac{45-8\sqrt3}{39}.
\]
The endpoint \(p=1\) does not satisfy the unsquared stationary equation. Direct substitution gives
\[
H'(0)>0,
\qquad
H'(1)<0.
\]
Because the squared stationary equation has no other roots, \(p_*\) is the unique interior stationary point and the unique global maximizer of \(H\), hence the unique global minimizer of \(E\).

At \(p_*\),
\[
S(p_*)=\frac{7+4\sqrt3}{16}
=
\frac{(2+\sqrt3)^2}{16},
\]
so
\[
\sqrt{S(p_*)}=\frac{2+\sqrt3}{4}.
\]
Substitution into \(E\) gives
\[
E_*=\frac{63-32\sqrt3}{117}.
\]

At \(p=1\),
\[
E(1)=\frac12-\frac{\sqrt3}{4},
\]
the one-way optimum identified by the source. Subtraction yields
\[
E(1)-E_*
=
\frac{11\sqrt3-18}{468}.
\]
This is positive because
\[
(11\sqrt3)^2=363>324=18^2.
\]

## Verification

`verify_double_trine_optimum.py` independently reconstructs \(P_0,P_1,P_2\), the overlap, \(Q\), \(S\), the exact candidate \(p_*\), and the exact values of \(E_*\) and the one-way gap using high-precision decimal arithmetic.

It checks the stationary equation at \(p_*\), verifies that the source endpoint \(p=1\) is not stationary, and evaluates a dense grid of \(200001\) points on \([0,1]\) as a supplementary numerical stress test. The grid check is not used as proof of global optimality; the proof is the exact stationary-factorization argument above.

## Relationship to prior work

Chitambar and Hsieh introduced the explicit adaptive protocol and derived the branch probabilities and Helstrom expression used here. Their figure plots the protocol error against \(p\), and the text states that the curve has a minimum of approximately
\[
6.47\times10^{-2},
\]
strictly below the optimal one-way value
\[
\frac12-\frac{\sqrt3}{4}.
\]
The inspected source does not state the optimizing \(p\), an exact radical value for the minimum, or an exact radical expression for the gap.

Their later work on asymptotic state discrimination places this example in a broader hierarchy of LOCC distinguishability norms and is indexed under quantum measurement theory. Later literature continues to cite the double-trine ensemble as a benchmark for separations among measurement classes.

Targeted searches using the exact decimal optimizer, the radical candidate, the exact minimum error, and combinations of “double trine,” “LOCC,” “measurement strength,” and “minimum error” did not locate the displayed exact optimization. The claim is therefore deliberately limited to the published one-parameter witness family and does not assert an exact optimum over all two-way LOCC protocols.

## Limitations

The exact value \(E_*\) is the optimum of this particular three-round one-parameter protocol family. It is an upper bound on the unrestricted two-way LOCC minimum error, not a proof that no more elaborate LOCC protocol can do better.

The derivation uses the symmetry and equal priors of the double-trine ensemble. Unequal priors or altered local trine states change both the posterior probabilities and the scalar optimization.

The literature search cannot rule out an equivalent exact simplification in unindexed notes, theses, or later work using different parameter conventions. The source itself provides the numerical minimum, so the originality claim is only the exact closed-form optimization and gap.

## References

1. E. Chitambar and M.-H. Hsieh, “A Return to the Optimal Detection of Quantum Information,” arXiv:1304.1555, first submitted 4 April 2013; published as “Revisiting the optimal detection of quantum information,” *Physical Review A* 88, 020302(R) (2013), DOI: 10.1103/PhysRevA.88.020302.
2. E. Chitambar and M.-H. Hsieh, “Asymptotic State Discrimination and a Strict Hierarchy in Distinguishability Norms,” arXiv:1311.1536; *Journal of Mathematical Physics* 55, 112204 (2014), DOI: 10.1063/1.4902027.
3. A. Peres and W. K. Wootters, “Optimal Detection of Quantum Information,” *Physical Review Letters* 66, 1119–1122 (1991), DOI: 10.1103/PhysRevLett.66.1119.
