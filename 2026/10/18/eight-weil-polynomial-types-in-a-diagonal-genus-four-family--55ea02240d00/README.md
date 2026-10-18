# Reproducing the diagonal genus-four twist calculation

Run `python3 src/verify.py` from the directory containing `src/` and `data/` using Python 3.8 or newer. The script requires only the standard library, constructs finite fields with exact modular integer arithmetic, enumerates the eighteen diagonal types over three different quadratic fields, and separately checks the second extension for the five-element prime field. It compares the computed tables byte-independently against the parsed numerical data in `data/expected.json` and raises an exception upon disagreement.

The finite-field checks do not prove the theorem for all primes. The general proof is given in `RESULT.md` via the Hermitian-to-Fermat-to-genus-four maps and the eight tame characters.
