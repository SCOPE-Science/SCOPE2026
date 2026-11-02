# Review of the ordered composite-DNA capacity improvement

## Correctness: PASS

The exact three-input, four-output transition matrix follows from two independent binary symmetric channels. Its conditional entropy is constant across inputs. Symmetry gives an optimal endpoint-balanced law and linear independence of the three rows guarantees uniqueness for strictly positive, nonmaximal noise. The derivative of output entropy has strictly negative second derivative, is positive at the repetition-only boundary, and negative at the pure mixed-symbol boundary. These facts prove the strict capacity gain over all \(0<p<1/2\). The noiseless and pure-noise endpoints are direct. An analytic implicit-function argument identifies the unique small-noise-contrast root; exact rational coefficient calculations check the sixth-, eighth-, and tenth-order gain coefficients. The supplied independent code paths verify the transition matrix and numerical and formal-series calculations, not the theorem by finite enumeration alone.

## Originality: PASS with priority risk

The directly relevant Dollma–Elishco–Yaakobi paper establishes the model, symmetry reduction, and numerical capacity comparison. The stronger statements here are the all-noise strict gap, unique interior optimum, and quantified sixth-order high-noise expansion. The multiple-read repetition channel lacks the mixed ordered symbol. Existing multinomial composite-DNA optimization concerns a different sampling law; the relevant 2025 journal article was available only through its bibliographic metadata and abstract. Search comparisons did not identify an equivalent all-noise theorem, but nonindexed or inaccessible literature could affect priority.

## Value: PASS

The ordered composite architecture offers an extra mixed information symbol, but at large bit-noise rates it appears to achieve nearly the same capacity as ordinary repetition. Showing an improvement at every nontrivial crossover rate and identifying the exact sixth-order suppression explains that phenomenon quantitatively, resolving a motivated analytic comparison rather than merely tabulating numerical optima.

## Limitations

The result does not provide an elementary closed capacity expression at all noise levels or optimize other ordered resolutions. Independent external mathematical validation and exhaustive publication-priority certification remain unperformed.

Self-review: passed. Independent audit: not yet performed.
