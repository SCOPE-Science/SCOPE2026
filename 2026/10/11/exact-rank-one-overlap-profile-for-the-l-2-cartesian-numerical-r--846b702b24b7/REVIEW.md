# Independent mathematical audit

## correctness

PASS

For any nonzero rank-one T=alpha u⊗v on a complex Hilbert space, scalar phase/unitary similarity reduce it (on span{u,v}) to the real 2x2 block alpha[[r,s],[0,0]], r=|tr T|/alpha in [0,1], s=sqrt(1-r²), with zero direct summand. Re(e^-itT) has eigenvalues alpha/2[r cos t ± sqrt(1-r² sin²t)]; since sqrt(1-r² sin²t)≥r|cos t|, the norm is exactly alpha/2(sqrt(1-r²sin²t)+r|cos t|). Its square is alpha²/4[1+r²cos2t+2r|cos t|sqrt(1-r²sin²t)]. The cos2t term averages to zero, and the cross term becomes (2/pi)int_0^1 sqrt(1-r²u²)du; evaluation yields omega_2²=alpha²[1/4+(r sqrt(1-r²)+asin r)/(2pi)]. r=0 gives alpha²/4, r=1 gives alpha²/2; no hidden division by zero since antiderivative at r=0 is taken by limit. Independent quadrature on the actual 2x2 Hermitian matrix at r=0,.07,.2,.5,.8,.999,1 matches to <=9e-13. Classical omega rank-one identity gives the asserted ratio, and r=0 iff T²=0, r=1 iff normal. This is a complete all-parameter symbolic proof, not extrapolated from sampling.

## originality

PASS

Best-of-knowledge PASS for the full continuous rank-one omega_2 profile, not for the defining integral, the classical rank-one omega formula, or either sharp endpoint alone. The focal Audeh–Moradi–Sahoo arXiv:2610.04844v1 defines omega_2 and proves universal inequalities and equality mechanisms; its exhibited upper-bound Pauli 2x2 example has determinant zero and trace zero, so a rank-one nilpotent saturating the upper bound is ALREADY implicit in that paper, while its self-adjoint equality includes rank-one projections at the lower bound. Nevertheless its inspected full HTML has no rank-one specialization or interior r-dependent arcsin identity. Denčić et al. arXiv:2503.05036v1 Theorem 2.1 treats a distinct constrained two-vector q-numerical radius and (1.2) the classical omega. Audeh–Kittaneh–Moradi arXiv:2610.15242v1 Theorem 2.2 concerns omega via a supremum over vector-state angular integrals rather than the average of OPERATOR norms defining omega_2; the two quantities cannot be identified by swapping sup and integral. Published Resultary normal-unitary spectral-gap and cubic-stability findings address different operator classes/aspects and do not imply the nonnormal rank-one continuum formula. A universal prior integral evaluation under another name remains a residual risk; a failed search is not treated as priority proof.

## value

PASS

An exact continuous profile for a just-introduced angular numerical-radius functional on the canonical rank-one family is a naturally motivated and independently usable benchmark, rather than an arbitrary tiny slice. Rank-one operators are a standard test class, and their normalized generating-vector overlap r is the unique scalar parameter after phase/unitary reductions. The formula gives the entire 0≤r≤1 transition (indeed d(omega_2²/alpha²)/dr=sqrt(1-r²)/pi), quantitatively interpolates between nilpotent and normal extremes, and allows evaluation/comparison without angular integration. The two endpoint examples themselves are already implicit in the original paper, so their rediscovery is not assigned independent value; the substantive surviving fact is the full interior function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
