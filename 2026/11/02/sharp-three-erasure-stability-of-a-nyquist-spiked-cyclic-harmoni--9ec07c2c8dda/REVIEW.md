# Mathematical review

## Correctness — PASS
The frame is Parseval by three distinct Fourier frequencies. The unitary parity-channel decomposition reduces every three-erasure Gram spectrum to either a two-dimensional rank-deficient block or a three-dimensional nonnegative tridiagonal block. The unit-root projection lemma gives the exact pure-parity maximum; three explicit positive-definiteness certificates, with leading minors \((2,4,12)\), \((2,2,4)\), and \((3,4,14)\), strictly exclude all mixed-parity competitors. The proof verifies the full set of extremizers, upper-bound equality, the boundary at \(m=3\), and the squared condition number. The standalone numerical checker independently evaluated 64,676 small-order erasure spectra without using them as an infinite proof.

## Originality — PASS under bounded comparison
The closest published result on **two-character** cyclic-frame erasures does not control the third Nyquist coordinate. The published full-spark criterion for \(\{0,1,r\}\) gives rank conditions on three selected columns, not sharp frame spectra after deleting three columns. The published consecutive-triple Riesz problem uses different frequency rows and optimizes a different spectral quantity. Bodmann–Paulsen establish general frame-erasure bounds, while Ferreira's 1994 work notes the contrast between lowpass and bandpass erasure geometry without an inspected exact statement for the present all-order Nyquist family. Osgood–Siripuram–Wu address universal interpolation rather than sharp quantitative conditioning. Complete Ferreira and Rath–Guillemot papers could not be inspected, so an implicit historical formula remains a specific originality risk; the searched evidence did not establish a stronger covering theorem.

## Mathematical value — PASS
A Nyquist mode is a canonical aliasing boundary in cyclic sampling, and its interaction with one baseband mode gives a natural three-frequency non-equiangular Parseval frame. The theorem supplies a sharp worst-erasure reconstruction constant at every even order, a complete extremizer census, and an exact injectivity threshold. Its worst masks are step-two rather than consecutive, a structural bandpass phenomenon relevant to deterministic erasure design. The result is not claimed for arbitrary bands, and no downstream performance guarantee beyond these frame bounds is asserted.

## Limitations
Scientific: Only this one natural three-row frequency pattern and exactly three deleted sites are treated. Existing full-spark results already imply certain qualitative dependence behavior. Access: the two plausible older engineering sources were only compared by available abstracts and author synopsis. Independent proof and originality evaluation have not been performed.

Self-review: passed. Independent audit: not yet performed.
