# Sharp all-degree threshold for a 4-periodic alternating-magnetism SOS branch
## Finding
For the SOS model with alternating magnetism on the Cayley tree of order \(k\ge2\), consider the translation-invariant 4-height-periodic boundary-law reduction used by Ganikhodjaev, Khatamov and Rozikov. In the variables \(u=x^{1/k}\), \(v=z^{1/k}\), \(w=y^{1/k}\), restrict their system to \(u=1\) and \(w=v>0\). The source notes that this produces
\[
F_{k,\theta}(v)=v^{k+1}-(\theta+1)v^k+(\theta+1)v-1=0,
\]
but it does not classify this equation for general \(k\ge3\).

Define
\[
\theta_4(k)=\frac{2}{k-1}.
\]
For every integer \(k\ge2\):

- if \(0<\theta\le\theta_4(k)\), the only positive root is \(v=1\);
- if \(\theta>\theta_4(k)\), there are exactly three positive roots, \(1\) and a reciprocal pair \(v_-=v_+^{-1}\ne1\).

Writing \(v_+=e^{2t}\), the nonconstant branch is parameterized exactly by the unique \(t>0\) satisfying
\[
\theta+1=\frac{\sinh((k+1)t)}{\sinh((k-1)t)}.
\]
The normalized 4-periodic laws are
\[
[1,1,e^{2kt},e^{2kt}]
\quad\text{and}\quad
[1,1,e^{-2kt},e^{-2kt}].
\]
A two-step cyclic shift of the first, followed by multiplication by the common scalar \(e^{-2kt}\), gives the second. Since cyclic height shifts and common positive rescaling do not change the mixed gradient measure, these two laws generate one translation-invariant gradient Gibbs measure.

At the threshold, \(v=1\) is a triple root. If \(r=v^k\) and \(\delta=\theta-\theta_4(k)>0\), then
\[
|\log r|
=
\sqrt{\frac{6k(k-1)}{k+1}}\,\sqrt{\delta}
+O(\delta^{3/2}).
\]
Thus the branch is a supercritical reciprocal pitchfork with an explicit all-degree onset amplitude.

## Assumptions and scope
The Cayley tree has order \(k\ge2\). The transfer parameter is the source parameter \(\theta>0\). Only translation-invariant, 4-height-periodic boundary laws in the source's graph-admissible alternating-magnetism model are considered, and only the subfamily \(u=1\), \(w=v\) is classified. The corresponding normalized boundary-law pattern is \([1,1,r,r]\) with \(r=v^k\).

The claim does not classify other solutions of the full three-variable 4-periodic system. It also does not assert extremality, reconstruction thresholds, stability, free-energy dominance, or a complete phase diagram.

## Proof
With \(u=1\) and \(w=v\), the first equation of the source's three-variable system is an identity, while the second and third both reduce to
\[
v(\theta+1+v^k)=1+(\theta+1)v^k,
\]
which is exactly \(F_{k,\theta}(v)=0\).

The root \(v=1\) is always present. For \(v\ne1\), rearrangement gives
\[
\theta+1=\frac{v^{k+1}-1}{v^k-v}.
\]
Put \(v=e^{2t}\). Cancellation of the common exponential factor yields
\[
\theta+1=A_k(t):=\frac{\sinh((k+1)t)}{\sinh((k-1)t)}.
\]
The function \(A_k\) is even. For \(t>0\),
\[
\frac{d}{dt}\log A_k(t)
=(k+1)\coth((k+1)t)-(k-1)\coth((k-1)t).
\]
The function \(h(s)=s\coth s\) is strictly increasing for \(s>0\), because
\[
h'(s)=\frac{\sinh s\cosh s-s}{\sinh^2s}
=\frac{\sinh(2s)-2s}{2\sinh^2s}>0.
\]
Therefore \(A_k\) is strictly increasing on \((0,\infty)\). Its endpoint values are
\[
\lim_{t\downarrow0}A_k(t)=\frac{k+1}{k-1},
\qquad
\lim_{t\to\infty}A_k(t)=\infty.
\]
Hence a positive \(t\) exists uniquely precisely when
\[
\theta+1>\frac{k+1}{k-1},
\]
that is, precisely when \(\theta>2/(k-1)\). Evenness gives exactly the reciprocal pair \(e^{\pm2t}\), and no other positive roots are possible because every positive \(v\ne1\) has the form \(e^{2t}\) for a unique nonzero real \(t\).

At \(\theta=2/(k-1)\), direct differentiation gives
\[
F_{k,\theta}(1)=F'_{k,\theta}(1)=F''_{k,\theta}(1)=0,
\qquad
\frac{d^3}{dv^3}F_{k,\theta}(1)=k(k+1)>0,
\]
so the central root is exactly triple. Expanding the hyperbolic ratio at \(t=0\) gives
\[
\theta(t)=\frac{2}{k-1}
+\frac{2k(k+1)}{3(k-1)}t^2+O(t^4).
\]
Thus, with \(\delta=\theta-2/(k-1)\),
\[
t=\sqrt{\frac{3(k-1)}{2k(k+1)}}\sqrt{\delta}+O(\delta^{3/2}).
\]
Since \(|\log r|=2k|t|\), the stated amplitude follows.

Finally, a two-step cyclic shift sends \([1,1,r,r]\) to \([r,r,1,1]\), and common rescaling by \(r^{-1}\) gives \([1,1,r^{-1},r^{-1}]\). In the boundary-law construction this common factor cancels in normalization, while cyclic height shifts are summed over in the mixed gradient measure. Hence the reciprocal pair represents one GGM.

## Verification
The accompanying `verify.py` independently checks, with exact rational arithmetic for \(2\le k\le100\), the critical derivative identities and the threshold value. It also reconstructs representative positive branches from the hyperbolic parameterization, substitutes them into all three source equations, verifies reciprocal roots, and checks the square-root onset numerically at several degrees. These finite checks corroborate the algebra; the all-\(k\) proof is the monotonicity argument above and does not rely on enumeration.

For \(k=2\), the threshold is \(\theta_4(2)=2\), agreeing with the source's explicitly solved binary-tree 4-periodic branch. This is a consistency check, not an independent proof of the general result.

## Relationship to prior work
Ganikhodjaev, Khatamov and Rozikov derive the full 4-periodic system and solve the binary-tree case. Their final remark explicitly observes that for general \(k\ge3\), the specialization \(u=1\), \(v=w\) reduces to the displayed polynomial. The paper does not provide the all-degree root classification, the exact threshold \(2/(k-1)\) for this branch, the hyperbolic parameterization, or the onset amplitude.

Haydarov and Rozikov study 4-periodic boundary laws for the standard SOS interaction, with a different recurrence. Their results do not imply the alternating-magnetism equation here. Haydarov and Ilyasova study a generalized SOS functional equation and obtain all 4-periodic laws in a specialized generalized model; their transfer rule and reduction are different and do not imply this branch classification. Published-record searches using the source equation, model aliases, threshold, reciprocal formulation, and hyperbolic form found no covering statement.

## Limitations
The result is branch-local. Other 4-periodic solutions of the alternating-magnetism three-variable system may exist outside \(u=1\), \(w=v\), and are not ruled out or counted here. Equality at the threshold produces only the constant law in this subfamily; the statement makes no claim about other branches at the same parameter. The GGM identification uses only cyclic shift and common boundary-law rescaling and does not establish extremality or distinctness from GGMs generated by unrelated boundary laws.

## References
1. N. N. Ganikhodjaev, N. M. Khatamov, U. A. Rozikov, “Gradient Gibbs measures of an SOS model with alternating magnetism on Cayley trees,” arXiv:2206.00245v1; Reports on Mathematical Physics 92 (2023), DOI:10.1016/S0034-4877(23)00082-4.
2. F. H. Haydarov, U. A. Rozikov, “Gradient Gibbs measures of an SOS model on Cayley trees: 4-periodic boundary laws,” arXiv:2110.10078v1; Reports on Mathematical Physics 90 (2022), DOI:10.1016/S0034-4877(22)00052-0.
3. F. H. Haydarov, R. A. Ilyasova, “Gradient Gibbs measures with periodic boundary laws of a generalized SOS model on a Cayley tree,” arXiv:2309.00867v1; Journal of Statistical Mechanics: Theory and Experiment (2023), DOI:10.1088/1742-5468/ad0a8b.
