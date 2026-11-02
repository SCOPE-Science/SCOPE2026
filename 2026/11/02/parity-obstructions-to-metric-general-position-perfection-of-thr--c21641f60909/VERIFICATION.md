---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limitations

The companion `verify.py` uses only the Python standard library. Run `python verify.py` in a directory containing that file. On the 13-vertex three-arm tree it reconstructs the original adjacency lists, enumerates all \(91\) geodesics of length at most \(8\), and checks the \((4,8)\)-clique condition for all vertex subsets using all \(4\)-subsets. The maximum clique size is \(9\). With the center color fixed to \(0\) by color-name permutation, all \(3^{12}=531441\) three-color assignments are checked against the three length-eight diameter paths and all fail. A concrete four-color assignment is checked against all geodesics and succeeds, so \(\chi_8^4=4\).

Expected terminal output:

```
THREE_COLOR_EXHAUSTIVE_FAIL_FIXED_CENTER 531441 assignments 3 diameter_paths
FOUR_COLOR_PATH_EXHAUSTIVE_OK 91 geodesics omega 9
VERIFY_OK
```

The infinite result for even \(k\ge4\) and odd \(q\ge3\) follows from the written argument, not the finite experiment. Its key noncomputational steps are: every larger-than-diameter clique meets three arms and fails the \(k\)-subpath property; any optimal \(q\)-palette coloring saturates the \(k-1\) occupancy ceiling on every diameter path; the three two-arm equations force an integer arm count equal to half an odd number. The general chromatic number is only bounded below, not claimed exact. Independent mathematical validation has not been carried out.
