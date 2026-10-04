# Review of Cross-ratio geometry and nodal singularities of the four-collinear line-multiview correction

## Correctness

**PASS.** The proof starts from the published four-collinear correction determinant and the published all-collinear vanishing-ideal theorem. Restriction to the baseline component kills every determinantal minor identically, leaving precisely the correction hypersurface. Exact expansion gives the bracket formula and the fixed-cross-ratio equation.

The key singularity calculation is structural rather than experimental: on an affine chart the correction is a quadratic form \(D\) whose Hessian \(H\) has common-shift kernel and whose every principal \(3\times3\) minor equals
\[
2\prod_{i<j}(v_j-v_i),
\]
which is nonzero for distinct camera parameters. Thus \(\nabla D=0\) exactly on the common-shift line, corresponding to the small diagonal. Simultaneous projective transformations cover the global boundary charts. The transverse equation is a rank-three quadratic form, giving an \(A_1\) node, and Serre's criterion gives normality.

Risk: the scheme-theoretic intersection statement depends on using the four-camera all-collinear ideal theorem, not merely the earlier set-theoretic exceptional-locus description. That theorem was inspected directly.

## Originality

**PASS.** The closest line-multiview sources state the extra collinear correction and establish the appropriate ideal-theoretic framework, but the inspected text does not state the cross-ratio interpretation, the exact small-diagonal singular locus, normality, or transverse \(A_1\) type. Targeted published-index and web searches for these formulations did not return a covering result.

Classical work on \(\mathrm{PGL}_2\)-orbit closures of point configurations is broader background and creates a genuine residual risk that an equivalent orbit-closure singularity statement exists in another language. The specific implication checked here is narrower: neither the cited line-multiview papers nor the located general bibliographic record supplies the identification of their four-collinear camera correction with this ordered fixed-cross-ratio divisor together with the stated Hessian singularity certificate.

## Value

**PASS.** The result turns an elimination-style correction equation into intrinsic projective geometry. It identifies what the correction does on the exact component that makes rank minors insufficient, and it classifies the entire singular locus and its transverse local type. This is useful for local geometry of non-generic camera arrangements, for understanding how the extra equation removes the determinantal component, and for future scheme-theoretic or numerical analyses near collinear degeneracies.

## Closest literature and limitations

The principal sources are arXiv:2203.01694 and arXiv:2303.02066. The former explains why four or more collinear cameras require additional constraints; the latter gives the determinant and proves the relevant extended ideal is radical and equals the vanishing ideal for collinear cameras. Aluffi--Faber (1993) is relevant general orbit-closure background. The claim is limited to distinct complex camera parameters and to the correction divisor inside the baseline component.

Same-model review: passed. Independent audit: not yet performed.
