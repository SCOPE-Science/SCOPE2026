# Same-model review

## Correctness

PASS. For every \(p\ge p_a\), the source's separated Hamilton--Jacobi construction extends verbatim with \(p\) in place of \(p_a\), and the sign conditions required for calibration remain valid. The endpoint increment is the stated \(F_n(a,p)\). Direct differentiation gives
\[
\partial_pF_n(a,p)=2\Psi_n(a,p),
\]
while the integral kernel defining \(\Psi_n\) strictly decreases with \(p\); hence \(F_n\) is strictly convex. The source's proved sign change of the minimal-momentum mismatch at \(a_n\) therefore gives the full phase transition.

For \(a>a_n\), the unique zero of \(\Psi_n(a,p)\) makes the incoming and reflected outgoing characteristics meet at \((\sqrt a,-\sqrt a)\). Their calibrated increments telescope, proving attainment. The boundary case \(a=1\) is forced onto horizontal and vertical sides and has zero action. Uniform large-\(p\) expansions establish both sharp asymptotic constants. The numerical checker is supplementary only.

## Originality

PASS. Remark 6.5 of the primary source already identifies variable momentum as the correct idea and states the qualitative location of the minimizer, so that portion is not claimed as new. The source explicitly leaves the auxiliary fixed-parameter problem undeveloped. It does not give the scalar objective \(F_n(a,p)\), the identity and strict convexity in \(p\), the unique closing equation in the post-threshold regime, the endpoint value, or the square-root boundary constants. Targeted searches did not locate a separate public source containing these statements.

## Value

PASS. The fixed-turning value is the natural constrained profile behind the source's global calibration. Solving it clarifies exactly how the sharp path degenerates after the source's closing threshold and quantifies the collapse at the boundary. The unique momentum and square-root law give reusable information about the Hamilton--Jacobi mechanism beyond the single globally optimizing parameter.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Shiri Artstein-Avidan, arXiv:2609.38041v1, especially Remark 6.5. It already sketches the variable-momentum strategy and qualitative phase. The present result should therefore be read as an explicit completion and endpoint analysis of that auxiliary problem, not as a new global Santaló inequality.

The theorem is restricted to the relaxed causal-curve problem at prescribed turning parameter. It does not change the global sharp constant or equality bodies of the source. A contemporaneous unindexed elaboration of Remark 6.5 remains the main bibliographic risk.
