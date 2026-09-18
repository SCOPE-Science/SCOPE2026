# Review

## Correctness

**PASS.** The proof uses Li--Zeng's all-dimensional companion-rectangle
decomposition before the final function-space estimate. Their two cases reduce
the mean oscillation on a \(\gamma\)-rectangle \(Q\) to parameter averages of
commutator outputs whose inputs have \(L^p\) size \(O(|Q|^{1/p})\), while the
relevant output subset has measure comparable to \(|Q|\). Replacing their
strong \(L^p\) estimate by the equivalent norm
\[
\|h\|_{q,\infty,*}
=\sup_F |F|^{-1/q'}\int_F|h|
\]
is legitimate for every \(q>1\): this norm is equivalent to weak \(L^q\),
translation invariant, and satisfies integral Minkowski. The resulting factor
is exactly \(|Q|^{1/p-1/q}\), which is the normalization defining
\(\operatorname{BMO}^{\gamma,\alpha}\) when
\(\alpha/|\beta|=1/p-1/q\).

The argument was stress-tested at \(q=p\), where it reduces to ordinary
anisotropic BMO, and at \(q>p\), where anisotropic dilation gives the same
Campanato scaling. The second Li--Zeng case uses a bounded, \(Q\)-supported
test function \(g\), so its \(L^p\) norm has the same \(|Q|^{1/p}\) scale.
No empirical computation is used in place of the proof.

## Originality

**PASS, to the best of our knowledge.** Li--Zeng (arXiv:2609.18613v1) prove
higher-dimensional necessity only for the diagonal \(L^p\to L^p\) problem.
Oikari (arXiv:2304.00621) proves off-diagonal sufficiency in arbitrary
dimension but explicitly restricts his necessity results to the plane.
Bongers--Guo--Li--Wick provide the earlier diagonal theory and testing-space
lower bound.

Searches using exact and synonymous combinations of monomial curves,
off-diagonal commutators, higher-dimensional necessity, weak type, Lorentz
targets, and anisotropic BMO/Campanato found these sources but no prior theorem
asserting weak \(L^p\to L^{q,\infty}\) necessity in all dimensions. The
current SCOPE archive was also checked by the mathematical object, source
identifiers, and equivalent terminology without finding an overlapping
record.

The main residual risk is recency: Li--Zeng's preprint is dated 16 September
2026, so an unindexed simultaneous observation could exist. No highly
relevant inaccessible source was identified.

## Value

**PASS.** The result closes the dimension gap in the off-diagonal necessity
direction and does so under the weaker Lorentz target hypothesis. Combined
with Oikari's existing strong sufficiency theorem, it yields an equivalence
between weak and strong off-diagonal boundedness throughout the established
all-dimensional sufficiency range. The new statement is not an interpolation
corollary: the Campanato exponent is generated directly by the mismatch
between the \(L^p\) input scale and the \(L^q\) major-subset scale.

## Limitations

The result is restricted to \(1<p\le q<\infty\) and monomial curves. It does
not extend Oikari's strong sufficiency range, and it does not address
\(q<p\), endpoints, compactness/VMO, weighted estimates, or general polynomial
curves. The higher-dimensional geometry is inherited from Li--Zeng's
companion-rectangle construction rather than reproved independently.

**Same-model review: passed. Cross-model review: not yet performed.**
