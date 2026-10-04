# Exact correlation-flow Markovianity threshold for the depolarizing–Ising competition model

## Finding

Consider the single-spin model of Apollaro, Lorenzo, Di Franco, Plastina, and Paternostro in which an Ising-coupled spin environment supplies memory while an independent isotropic depolarizing channel supplies Markovian noise. The source sets
\[
\gamma_x=\gamma_y=\gamma_z=\frac{\gamma_0}4,
\qquad
\alpha=\beta=0,
\]
and uses
\[
z=2B^{0}_{--}-1.
\]
Because the reduced dynamics is even in \(z\), write
\[
z=|2B^{0}_{--}-1|\in[0,1].
\]
Assume \(J\ne0\), introduce dimensionless time and noise strength
\[
u=|J|t,
\qquad
\gamma=\frac{\gamma_0}{|J|},
\]
and use the Luo–Fu–Song correlation-flow witness employed in the source.

Then its exact onset-of-Markovianity threshold is
\[
\boxed{
\gamma^*_{\mathrm{LFS}}(z)
=
\frac{1-z^2}{\sqrt{3(1+2z^2)}}
}.
\]
Precisely, the LFS non-Markovianity vanishes if and only if
\[
\gamma\ge\gamma^*_{\mathrm{LFS}}(z),
\]
and it is positive whenever
\[
0\le\gamma<\gamma^*_{\mathrm{LFS}}(z).
\]
Restoring dimensions,
\[
\gamma^*_{0,\mathrm{LFS}}(z)
=
|J|\frac{1-z^2}{\sqrt{3(1+2z^2)}}.
\]

The maximum over the initial memory-spin polarization is therefore
\[
\boxed{
\max_{0\le z\le1}\gamma^*_{\mathrm{LFS}}(z)
=
\frac1{\sqrt3}
=0.577350269189\ldots
},
\]
attained at \(z=0\). This is the exact value behind the source's numerical statement that the correlation-flow witness becomes Markovian for a universal rate of approximately \(0.6\).

The formula also analytically reproduces the source's threshold hierarchy. For \(0<z\le1\), the source gives
\[
\gamma^*_{\mathrm{LPP}}(z)=\frac{1-z^2}{3z},
\]
and the exact ratio is
\[
\frac{\gamma^*_{\mathrm{LFS}}}{\gamma^*_{\mathrm{LPP}}}
=
\frac{\sqrt3\,z}{\sqrt{1+2z^2}}
\le1,
\]
with equality only at \(z=1\).

## Assumptions and scope

The result concerns exactly the isotropic depolarizing channel and two-spin Ising memory model used in the source. The parameter \(\gamma\) is the depolarizing rate in units of the absolute Ising coupling \(|J|\). The result uses the simplified Luo–Fu–Song witness obtained from the quantum mutual information between the system and an initially maximally entangled ancilla, exactly as in the source's equation for \(X_{\mathrm{LFS}}\).

“Markovian” here means Markovian according to this correlation-flow witness: its mutual-information rate is nowhere positive, so the corresponding integrated non-Markovianity measure is zero. It does not mean that the channel is CP-divisible according to every other definition. The source itself emphasizes that different witnesses have different thresholds.

The theorem does not cover the source's more general amplitude-damping-plus-depolarizing appendix, arbitrary Kossakowski matrices, multi-spin memory environments, or alternative non-Markovianity measures.

## Proof

With \(u=|J|t\), set
\[
q=e^{-\gamma u}
\]
and
\[
r(u,z)
=
\sqrt{\cos^2u+z^2\sin^2u}
=
\sqrt{1-(1-z^2)\sin^2u}.
\]
The source's functions become
\[
f=\frac{1+q}2,
\qquad
|G|=qr.
\]
For the system-ancilla state entering the LFS mutual information, define
\[
a=\frac{1-q}4,
\qquad
b=\frac{1+q+2qr}4,
\qquad
c=\frac{1+q-2qr}4.
\]
Its spectrum is \(a,a,b,c\), while both marginals are maximally mixed. Therefore the mutual information is
\[
I(q,r)
=
2+2a\log_2 a+b\log_2 b+c\log_2 c.
\]
For \(0<q<1\), differentiation gives
\[
I_q
=
\frac{-2\ln a+(1+2r)\ln b+(1-2r)\ln c}{4\ln2}
\]
and
\[
I_r
=
\frac{q}{2\ln2}\ln\frac bc.
\]
Both are nonnegative, and \(I_q>0\) for \(q>0\). One direct way to see the latter is to write
\[
I(q,r)=\frac1{\ln2}D\!\left(p(q,r)\middle\|\left(\frac14,\frac14,\frac14,\frac14\right)\right),
\]
where \(p(q,r)=(a,a,b,c)\) is affine in \(q\). The derivative vanishes at \(q=0\), while the second derivative is strictly positive for nontrivial \(p\).

The key estimate is
\[
\boxed{
\frac{I_r}{qI_q}
\le
\frac{2r}{1+2r^2}
}.
\]
To prove it, the inequality is equivalent to
\[
c^{1+r}\ge b^{1-r}a^{2r}.
\]
After cancelling the common factor \(4^{-(1+r)}\), put
\[
A=1-q,
\qquad
B=1+q+2qr,
\qquad
C=1+q-2qr.
\]
With weights
\[
\lambda=\frac{1-r}{1+r},
\qquad
1-\lambda=\frac{2r}{1+r},
\]
weighted AM–GM gives
\[
B^\lambda A^{1-\lambda}
\le
\lambda B+(1-\lambda)A
=C.
\]
This proves the estimate.

The estimate is asymptotically sharp as \(q\downarrow0\). Indeed,
\[
I(q,r)
=
\frac{q^2(1+2r^2)}{2\ln2}+O(q^3),
\]
so
\[
\frac{I_r}{qI_q}
\longrightarrow
\frac{2r}{1+2r^2}.
\]

Now
\[
\frac{dI}{du}
=-\gamma qI_q+r'I_r.
\]
Whenever \(r'\le0\), this derivative cannot be positive. Put
\[
k=1-z^2
\]
and, on a rising branch of \(r\), set
\[
y=\sin^2u.
\]
Then
\[
2rr'=2k\sqrt{y(1-y)}
\]
and therefore
\[
\frac{r'I_r}{qI_q}
\le
F_z(y)
:=
\frac{2k\sqrt{y(1-y)}}{3-2ky}.
\]
A single differentiation gives the unique interior maximizer
\[
y_*
=
\frac3{2(3-k)}
=
\frac3{2(2+z^2)}.
\]
Substitution yields
\[
\max_{0\le y\le1}F_z(y)
=
\frac{1-z^2}{\sqrt{3(1+2z^2)}}.
\]
Hence, if \(\gamma\) is at least the displayed threshold, then \(dI/du\le0\) at every time and the LFS measure is zero.

For sharpness, assume first
\[
0<\gamma<\gamma^*_{\mathrm{LFS}}(z)
\]
and \(z<1\). Choose the repeated rising-branch phases
\[
u_n
=
\pi-\arcsin\sqrt{y_*}+2\pi n.
\]
At every \(u_n\), the geometric factor equals its maximum, while
\[
q_n=e^{-\gamma u_n}\longrightarrow0.
\]
Because the information-theoretic estimate becomes equality in this limit, the local positivity threshold tends to \(\gamma^*_{\mathrm{LFS}}(z)\). Thus \(dI/du>0\) for all sufficiently large \(n\), proving positive LFS non-Markovianity. If \(\gamma=0\) and \(z<1\), the recurrent rise of \(r\) directly gives recurrent increases of \(I\). For \(z=1\), \(r\equiv1\) and the threshold is zero. This proves the iff statement on the full domain.

## Verification

`verify_lfs_threshold.py` independently evaluates the mutual information derivatives in a numerically stable form. It tests the weighted-AM–GM ratio bound on a deterministic grid of \(q\) and \(r\), reconstructs the analytic maximizer of the geometric factor, checks the source value \(z=0\), and verifies the LFS-versus-LPP hierarchy.

It also samples the full time-dependent mutual-information rate above the exact threshold and searches repeated rising branches below it. These finite calculations are supplementary; the all-time and all-parameter statement is supplied by the proof above.

## Relationship to prior work

Apollaro, Lorenzo, Di Franco, Plastina, and Paternostro derive compact rate expressions for four non-Markovianity witnesses in the competing depolarizing–Ising model. They obtain analytic thresholds for the RHP, BLP, and LPP witnesses. For the correlation-flow witness they explicitly state that the expression does not allow an analytical treatment in their analysis, evaluate the Markovianity threshold numerically, and report a universal threshold of approximately \(0.6\) at \(z=0\).

Luo, Fu, and Song introduced the underlying mutual-information correlation-flow measure. The present result does not modify that definition; it solves the specific scalar threshold problem left numerical in the competing-channel model.

Addis, Bylicka, Chruściński, and Maniscalco later compare several non-Markovianity measures in other exactly solvable one- and two-qubit dephasing and dissipative models. Their inspected public manuscript metadata and LFS discussion concern those reservoir models rather than the depolarizing–Ising competition analyzed here.

Targeted searches using the exact model title, the LFS acronym, the source identifier, the candidate radical, the value \(1/\sqrt3\), and combinations of “analytic threshold,” “depolarizing,” “Ising,” and “mutual information” did not locate the displayed formula. The originality claim is restricted to this exact threshold and its analytic proof for the source model.

## Limitations

The theorem is witness-specific. A channel can be Markovian according to LFS while remaining non-Markovian according to a stronger witness, exactly as the source's nested threshold diagram illustrates.

The proof uses the isotropic depolarizing specialization and a single Ising-coupled memory spin. The source's amplitude-damping-plus-depolarizing extension has a different mutual-information state and is not covered.

A residual literature risk remains because an equivalent threshold could appear in unindexed notes, theses, or later work using different notation. The direct source itself is decisive that its published LFS boundary was obtained numerically rather than analytically.

## References

1. T. J. G. Apollaro, S. Lorenzo, C. Di Franco, F. Plastina, and M. Paternostro, “Competition between memory-keeping and memory-erasing decoherence channels,” arXiv:1311.2045, first submitted 8 November 2013; *Physical Review A* 90, 012310 (2014), DOI: 10.1103/PhysRevA.90.012310.
2. S. Luo, S. Fu, and H. Song, “Quantifying non-Markovianity via correlations,” *Physical Review A* 86, 044101 (2012), DOI: 10.1103/PhysRevA.86.044101.
3. C. Addis, B. Bylicka, D. Chruściński, and S. Maniscalco, “Comparative study of non-Markovianity measures in exactly solvable one- and two-qubit models,” arXiv:1402.4975; *Physical Review A* 90, 052103 (2014), DOI: 10.1103/PhysRevA.90.052103.
